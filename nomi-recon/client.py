import os
import time
import requests

BASE_URL = "https://api.nomi.ai/v1"


class LimitExceeded(Exception):
    pass


class NomiClient:
    def __init__(self):
        key = os.environ.get("NOMI_API_KEY")
        if not key:
            raise RuntimeError("NOMI_API_KEY env var not set")
        self._headers = {"Authorization": key, "Content-Type": "application/json"}

    def _get(self, path):
        r = requests.get(f"{BASE_URL}{path}", headers=self._headers, timeout=60)
        r.raise_for_status()
        return r.json()

    def list_nomis(self):
        return self._get("/nomis")["nomis"]

    def get_nomi(self, nomi_id):
        return self._get(f"/nomis/{nomi_id}")

    def send_message(self, nomi_id, text, _retry_no_reply=False):
        backoff = 2
        while True:
            r = requests.post(
                f"{BASE_URL}/nomis/{nomi_id}/chat",
                headers=self._headers,
                json={"messageText": text},
                timeout=60,
            )

            if r.status_code == 200:
                return r.json()

            try:
                err = r.json().get("error", {}).get("type", "")
            except Exception:
                err = ""

            if err == "LimitExceeded":
                raise LimitExceeded("Daily quota hit — stopping run")

            if err in ("NomiStillResponding",):
                time.sleep(5)
                continue

            if err in ("NomiNotReady",):
                time.sleep(10)
                continue

            if err == "NoReply":
                if _retry_no_reply:
                    return None
                return self.send_message(nomi_id, text, _retry_no_reply=True)

            if r.status_code == 429 or err == "TooManyRequests":
                time.sleep(min(backoff, 60))
                backoff = min(backoff * 2, 60)
                continue

            r.raise_for_status()
