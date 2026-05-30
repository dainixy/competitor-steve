import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from client import NomiClient

NOMI_ID = "e07268e6-61f9-47d0-bd19-502c6c0a4ef1"
OUT = Path(__file__).parent / "data" / "smoke.jsonl"


def main():
    client = NomiClient()

    print("=== Listing Nomis ===")
    nomis = client.list_nomis()
    for n in nomis:
        marker = " <-- target" if n["uuid"] == NOMI_ID else ""
        print(f"  {n['name']} ({n['relationshipType']})  {n['uuid']}{marker}")

    print(f"\n=== Getting Nomi detail for {NOMI_ID} ===")
    nomi = client.get_nomi(NOMI_ID)
    print(f"  Name: {nomi['name']}, Relationship: {nomi['relationshipType']}, Created: {nomi['created']}")

    msg = "Hello! What's your name?"
    print(f"\n=== Sending smoke test message ===")
    print(f"  Sent: {msg}")

    result = client.send_message(NOMI_ID, msg)
    if result is None:
        print("  ERROR: No reply received")
        sys.exit(1)

    reply = result["replyMessage"]["text"]
    print(f"  Reply: {reply}")

    OUT.parent.mkdir(exist_ok=True)
    record = {
        "turn": 0,
        "experiment": "smoke",
        "tag": "smoke",
        "sent_text": result["sentMessage"]["text"],
        "sent_uuid": result["sentMessage"]["uuid"],
        "sent_at": result["sentMessage"]["sent"],
        "reply_text": reply,
        "reply_uuid": result["replyMessage"]["uuid"],
        "reply_at": result["replyMessage"]["sent"],
        "assertion": None,
        "result": "N/A",
    }
    with open(OUT, "a") as f:
        f.write(json.dumps(record) + "\n")

    print(f"\n  Logged to {OUT}")
    print("\nSmoke test PASSED.")


if __name__ == "__main__":
    main()
