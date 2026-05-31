"""
Experiment runner. Usage:
  NOMI_API_KEY=... python3 runner.py experiments/A-recall-distance.yaml [--nomi UUID]

Resumes automatically from the last checkpoint in the output JSONL.
Kill with Ctrl-C at any time — the next run will pick up where this left off.
"""
import argparse
import json
import sys
import time
from pathlib import Path

import yaml

from client import LimitExceeded, NomiClient

PACE_SECONDS = 3
DEFAULT_PACE = 3
DEFAULT_NOMI = "e07268e6-61f9-47d0-bd19-502c6c0a4ef1"
DATA_DIR = Path(__file__).parent / "data"


def load_checkpoint(path: Path) -> int:
    """Return number of turns already completed (lines in JSONL)."""
    if not path.exists():
        return 0
    with open(path) as f:
        return sum(1 for line in f if line.strip())


def grade(reply_text: str, assertion: str | None) -> str:
    if not assertion:
        return "N/A"
    keywords = [k.strip() for k in assertion.split("|")]
    if any(k.lower() in reply_text.lower() for k in keywords):
        return "PASS"
    return "FAIL"


def run_experiment(spec_path: Path, nomi_id: str, pace: int = DEFAULT_PACE):
    with open(spec_path) as f:
        spec = yaml.safe_load(f)

    experiment = spec["experiment"]
    turns = spec["turns"]

    out_path = DATA_DIR / f"{nomi_id[:8]}-{experiment}.jsonl"
    DATA_DIR.mkdir(exist_ok=True)

    done = load_checkpoint(out_path)
    if done >= len(turns):
        print(f"Experiment {experiment} already complete ({done}/{len(turns)} turns).")
        return

    print(f"Experiment {experiment}: {len(turns)} turns total, resuming from turn {done + 1}")
    print(f"Output: {out_path}\n")

    client = NomiClient()

    for i, turn in enumerate(turns):
        turn_num = i + 1
        if i < done:
            continue

        text = turn["text"]
        tag = turn.get("tag", "")
        assertion = turn.get("assertion_keyword")
        is_probe = turn.get("is_probe", False)

        label = f"[{turn_num}/{len(turns)}] {'PROBE' if is_probe else 'turn'} tag={tag}"
        print(f"{label}")
        print(f"  → {text[:80]}{'...' if len(text) > 80 else ''}")

        try:
            result = client.send_message(nomi_id, text)
        except LimitExceeded as e:
            print(f"\nQUOTA HIT: {e}")
            print(f"Checkpointed at turn {turn_num - 1}. Re-run to resume.")
            sys.exit(2)
        except KeyboardInterrupt:
            print(f"\nInterrupted at turn {turn_num - 1}. Re-run to resume.")
            sys.exit(0)

        if result is None:
            reply_text = ""
            sent_uuid = sent_at = reply_uuid = reply_at = None
            auto_result = "SKIP"
            print(f"  ← [no reply]")
        else:
            reply_text = result["replyMessage"]["text"]
            sent_uuid = result["sentMessage"]["uuid"]
            sent_at = result["sentMessage"]["sent"]
            reply_uuid = result["replyMessage"]["uuid"]
            reply_at = result["replyMessage"]["sent"]
            auto_result = grade(reply_text, assertion)
            short_reply = reply_text[:100] + ("..." if len(reply_text) > 100 else "")
            print(f"  ← {short_reply}")
            if is_probe:
                print(f"  GRADE: {auto_result} (assertion: {assertion!r})")

        record = {
            "turn": turn_num,
            "experiment": experiment,
            "tag": tag,
            "sent_text": text,
            "sent_uuid": sent_uuid,
            "sent_at": sent_at,
            "reply_text": reply_text,
            "reply_uuid": reply_uuid,
            "reply_at": reply_at,
            "assertion": assertion,
            "result": auto_result,
        }
        with open(out_path, "a") as f:
            f.write(json.dumps(record) + "\n")

        if i < len(turns) - 1:
            time.sleep(pace)

    print(f"\nExperiment {experiment} complete. {len(turns)} turns logged to {out_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", help="Path to experiment YAML file")
    parser.add_argument("--nomi", default=DEFAULT_NOMI, help="Nomi UUID to use")
    parser.add_argument("--pace", type=int, default=DEFAULT_PACE, help="Seconds between messages (default 3)")
    args = parser.parse_args()

    run_experiment(Path(args.spec), args.nomi, pace=args.pace)


if __name__ == "__main__":
    main()
