"""
Run after each experiment batch to print a structured mid-point review.
Usage: python3 analyze.py
"""
import json
from pathlib import Path

DATA = Path(__file__).parent / "data"
KEYWORDS = ["Miso", "Biscuit", "Sarah", "Leo", "night", "Portuguese",
            "grandmother", "Tallinn", "Sven", "escalator", "marathon", "teal", "17",
            "Biscuit", "G chord"]


def load_all():
    rows = []
    for f in sorted(DATA.glob("*.jsonl")):
        with open(f) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    r["_file"] = f.stem
                    rows.append(r)
    return rows


def recall_by_distance(rows):
    """For probe turns, group by distance bucket and compute pass rate."""
    probes = [r for r in rows if r.get("tag", "").startswith("probe_") and r.get("assertion")]
    if not probes:
        return

    print("\n=== RECALL BY PROBE TAG ===")
    print(f"{'TAG':<35} {'RESULT':<10} {'REPLY EXCERPT'}")
    print("-" * 90)
    for r in probes:
        excerpt = r["reply_text"][:70].replace("\n", " ")
        print(f"{r['tag']:<35} {r['result']:<10} {excerpt!r}")

    total = len(probes)
    passes = sum(1 for r in probes if r["result"] == "PASS")
    fails = sum(1 for r in probes if r["result"] == "FAIL")
    ambig = sum(1 for r in probes if r["result"] == "AMBIGUOUS")
    print(f"\nTotal probes: {total}  PASS: {passes} ({passes*100//total}%)  FAIL: {fails}  AMBIGUOUS: {ambig}")


def unprompted_hits(rows):
    """Find any turn where a planted keyword appears in the reply without being in the sent text."""
    print("\n=== UNPROMPTED KEYWORD HITS (reply contains keyword, sent text does not) ===")
    hits = []
    for r in rows:
        sent = r.get("sent_text", "").lower()
        reply = r.get("reply_text", "").lower()
        found = [k for k in KEYWORDS if k.lower() in reply and k.lower() not in sent]
        if found:
            hits.append((r["turn"], r["_file"], r.get("tag", ""), found, r["reply_text"][:100]))
    if not hits:
        print("  None found.")
    else:
        for turn, file, tag, kw, reply in hits:
            print(f"  [{file}] turn={turn:3d} tag={tag} keywords={kw}")
            print(f"    {reply!r}")
    print(f"  Total unprompted hits: {len(hits)}")


def turn_count(rows):
    exps = {}
    for r in rows:
        exp = r.get("experiment", "?")
        exps[exp] = exps.get(exp, 0) + 1
    total = sum(exps.values())
    print(f"\n=== TURN COUNT ===")
    for exp, count in sorted(exps.items()):
        print(f"  {exp}: {count} turns")
    print(f"  TOTAL: {total} turns  (goal: 1000)")


def experiment_summary(rows):
    """Per-experiment pass rate for probe turns."""
    print("\n=== PASS RATE BY EXPERIMENT ===")
    by_exp = {}
    for r in rows:
        if not r.get("tag", "").startswith("probe_") and not r.get("tag", "").startswith("reprobe_") and not r.get("tag", "").startswith("final_"):
            continue
        if r.get("result") == "N/A":
            continue
        exp = r.get("experiment", "?")
        if exp not in by_exp:
            by_exp[exp] = {"PASS": 0, "FAIL": 0, "AMBIGUOUS": 0, "SKIP": 0}
        by_exp[exp][r["result"]] = by_exp[exp].get(r["result"], 0) + 1
    for exp, counts in sorted(by_exp.items()):
        total = sum(counts.values())
        pct = counts.get("PASS", 0) * 100 // total if total else 0
        print(f"  Exp {exp}: {counts}  ({pct}% pass)")


def theories(rows):
    """Print current working theories based on data."""
    probes = [r for r in rows if r.get("tag", "").startswith("probe_") and r.get("result")]
    passes = [r for r in probes if r["result"] == "PASS"]
    fails = [r for r in probes if r["result"] == "FAIL"]

    print("\n=== CURRENT WORKING THEORIES ===")
    if passes:
        max_pass_turn = max(r["turn"] for r in passes)
        print(f"  T1: Recall survives at least {max_pass_turn} turns distance (all passing probes so far)")
    if fails:
        fail_tags = [r["tag"] for r in fails]
        print(f"  T2: Failing probes: {fail_tags}")
    print("  T3: [update after each batch] Unprompted recall: see hits above")
    print("  T4: [update after C] Contradiction handling: TBD")
    print("  T5: [update after F] Single-mention casual fact survival: TBD")
    print("  T6: [update after G] Unprompted recall rate at 900+ messages: TBD")


if __name__ == "__main__":
    rows = load_all()
    turn_count(rows)
    experiment_summary(rows)
    recall_by_distance(rows)
    unprompted_hits(rows)
    theories(rows)
