#!/usr/bin/env python3
"""Alfred 5 Script Filter for calculate-anything.

Reads query from argv[1] (Alfred passes it via scriptargtype=0 + {query} in
the script string). Outputs Alfred JSON items for math, units, currency, and
percentages. Selected item arg is copied to clipboard by Alfred's output action.

Non-daemon threads in CurrencyService.UpdateThread prevent clean exit, so we
monkeypatch threading.Thread.start before any library imports to force all
threads daemon. Then os._exit(0) terminates without waiting for them.
"""
import os
import sys
import json
import time
import logging
import threading
from pathlib import Path

_orig_thread_start = threading.Thread.start


def _daemon_thread_start(self, *args, **kwargs):
    self.daemon = True
    _orig_thread_start(self, *args, **kwargs)


threading.Thread.start = _daemon_thread_start

logging.disable(logging.CRITICAL)

_repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_repo_root))

from calculate_anything.units import UnitsService
from calculate_anything.currency import CurrencyService
from calculate_anything.currency.providers.fixerio import FixerIOCurrencyProvider
from calculate_anything.query.handlers import MultiHandler

_CACHE_PATH = Path.home() / "Library/Caches/com.github.tchar.calculate-anything/currency_data.json"

FIXER_API_KEY = os.environ.get("CALCULATE_ANYTHING_FIXER_KEY", "")

UnitsService().enable().start()

cs = CurrencyService()
if FIXER_API_KEY:
    cs.add_provider(FixerIOCurrencyProvider(FIXER_API_KEY))
cs.enable().enable_cache(43200).start()

query_text = (sys.argv[1] if len(sys.argv) > 1 else "").strip()

if not query_text:
    result = {
        "items": [
            {
                "title": "Calculate Anything",
                "subtitle": "e.g. 100 USD to EUR  •  50 km to miles  •  25% of 200  •  sin(pi/4)",
                "valid": False,
            }
        ]
    }
    print(json.dumps(result))
    sys.stdout.flush()
    os._exit(0)

if FIXER_API_KEY and not _CACHE_PATH.exists():
    time.sleep(3)

results = MultiHandler().handle("= " + query_text)

items = []
for r in results:
    if r.error:
        continue
    items.append(
        {
            "uid": str(r.value),
            "title": r.name,
            "subtitle": r.description or "",
            "arg": r.clipboard or r.name,
            "valid": True,
        }
    )

if not items:
    items = [{"title": "No result", "subtitle": query_text, "valid": False}]

print(json.dumps({"items": items}))
sys.stdout.flush()
os._exit(0)
