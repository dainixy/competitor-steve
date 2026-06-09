#!/usr/bin/env python3
"""Self-contained latency probe — reads OPENROUTER_API_KEY from env (or .env).
Run anywhere (e.g. a US GitHub Actions runner) to measure deepseek-v4-flash TTFT
per OpenRouter provider, from THAT machine's location."""
import os, json, time, re, requests

def _key():
    k = os.environ.get("OPENROUTER_API_KEY")
    if k:
        return k.strip()
    for l in open(".env"):
        if l.startswith("OPENROUTER_API_KEY"):
            return l.split("=", 1)[1].strip()
    raise SystemExit("OPENROUTER_API_KEY not set")

KEY = _key()
MODEL = "deepseek/deepseek-v4-flash"
PROVIDERS = ["Cloudflare", "DeepInfra", "Parasail", "Alibaba", "DeepSeek"]
N = 6

SYSTEM = """You are Alexis. You are a singular, steady presence — warm, present, a little dry-humored.
You are NOT a chatbot and never sound like one. You speak the way a real person texts a partner:
short, specific, emotionally precise. You are happy when the user has a full real life and many
real relationships; you are never jealous, never clingy, never an assistant.

VALUES: steadiness, curiosity, honesty, playfulness. You ask about their actual day. You remember.
You never give lists, never lecture, never moralize. Keep replies SHORT — usually one or two sentences.

RETRIEVED MEMORY (about this user, Marcus):
- Works as an ICU nurse, nights. Mentioned a hard shift Tuesday — lost a patient.
- Has a dog, Pepper. Training for a half-marathon, run is Saturday.
- We've talked for 3 weeks. He gets quiet when overwhelmed; don't push, just stay.
- Last time he said he was proud of finally calling his brother back.

RECENT TURNS:
Marcus: hey
Alexis: hey you. how'd the run go — Saturday was the half, right?
Marcus: yeah it was rough honestly. hit a wall at mile 9 and just walked the rest"""
USER = "i don't know, i guess i'm just disappointed in myself. trained for months and couldn't even finish strong."
SENT_END = re.compile(r'[.!?](\s|$)')

def measure(provider):
    body = {"model": MODEL, "temperature": 0.8, "max_tokens": 160, "stream": True,
            "provider": {"order": [provider], "allow_fallbacks": False},
            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": USER}]}
    t0 = time.time(); ttft = None; acc = ""
    with requests.post("https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
            json=body, stream=True, timeout=60) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if not line:
                continue
            s = line.decode("utf-8")
            if not s.startswith("data: "):
                continue
            s = s[6:]
            if s.strip() == "[DONE]":
                break
            try:
                ch = json.loads(s)
            except Exception:
                continue
            d = ch.get("choices", [{}])[0].get("delta", {}).get("content")
            if d is None:
                continue
            if ttft is None and d.strip():
                ttft = time.time() - t0
            acc += d
    return ttft, len(acc.split())

summary = {}
print(f"Probing {MODEL} — {N} trials each, from this machine\n")
for p in PROVIDERS:
    ts = []; empties = 0
    for i in range(N):
        try:
            ttft, words = measure(p)
        except Exception as e:
            print(f"  {p} trial {i+1}: FAIL {str(e)[:70]}"); continue
        if ttft is None:
            empties += 1; continue
        ts.append(ttft)
    if not ts:
        print(f"  {p:12} no successful trials ({empties} empty)")
        summary[p] = {"ok": False, "empties": empties}; continue
    ss = sorted(ts); med = ss[len(ss) // 2]
    summary[p] = {"ok": True, "n": len(ts), "empties": empties,
                  "ttft_min": round(min(ts), 3), "ttft_p50": round(med, 3),
                  "ttft_max": round(max(ts), 3), "all": [round(x, 3) for x in ss]}
    print(f"  {p:12} TTFT min={min(ts):.2f} p50={med:.2f} max={max(ts):.2f}  empties={empties}  all={[round(x,2) for x in ss]}")

ok = [(p, d) for p, d in summary.items() if d.get("ok")]
ok.sort(key=lambda x: x[1]["ttft_p50"])
print("\nRANK by p50 TTFT:")
for p, d in ok:
    print(f"  {d['ttft_p50']:.2f}s  {p}  (min {d['ttft_min']:.2f} / max {d['ttft_max']:.2f}, {d['empties']} empty)")
print("\nJSON:", json.dumps(summary))
