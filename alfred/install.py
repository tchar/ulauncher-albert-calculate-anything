#!/usr/bin/env python3
"""Install the Calculate Anything Alfred 5 workflow.

Creates a workflow in Alfred's preferences directory with two keyword triggers:
  calc <expr>  — calculate (math, units, currency, %; copies result)
  =    <expr>  — same (disable Alfred's built-in calculator first: Features → Calculator)

The workflow runs calculate.py from this directory using the venv at
VENV_PATH (default: ~/.venvs/alfred-calc). Create it once with:

    python3 -m venv ~/.venvs/alfred-calc
    ~/.venvs/alfred-calc/bin/pip install Pint>=0.17,<=0.23 simpleeval==0.9.13 \\
        parsedatetime==2.6 pytz==2021.1

Optionally set CALCULATE_ANYTHING_FIXER_KEY (fixer.io API key) in the workflow
environment for live currency conversion.
"""
import os
import plistlib
import shutil
import uuid
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VENV_PATH = Path.home() / ".venvs/alfred-calc"
PYTHON = VENV_PATH / "bin/python"

WORKFLOW_ID = "user.workflow.calculate-anything"
WORKFLOW_DIR = Path.home() / "Library/Application Support/Alfred/Alfred.alfredpreferences/workflows" / WORKFLOW_ID


def _uid():
    return str(uuid.uuid4()).upper()


def _script_filter(uid, keyword, title, subtext, python_bin, script_path):
    script = f'{python_bin} "{script_path}" "{{query}}" 2>/tmp/alfred_calc.log'
    return {
        "config": {
            "alfredfiltersresults": False,
            "alfredfiltersresultsmatchmode": 0,
            "argumenttype": 1,
            "escaping": 0,
            "keyword": keyword,
            "queuedelaycustom": 3,
            "queuedelayimmediatelyinitially": True,
            "queuedelaymode": 0,
            "queuemode": 1,
            "runningsubtext": "Calculating...",
            "script": script,
            "scriptargtype": 0,
            "scriptfile": "",
            "subtext": subtext,
            "title": title,
            "type": 0,
            "withspace": True,
        },
        "type": "alfred.workflow.input.scriptfilter",
        "uid": uid,
        "version": 3,
    }


def _clipboard_output(uid):
    return {
        "config": {
            "autopaste": False,
            "clipboardtext": "{query}",
        },
        "type": "alfred.workflow.output.clipboard",
        "uid": uid,
        "version": 3,
    }


def _connection(dest_uid):
    return [{"destinationuid": dest_uid, "modifiers": 0, "modifiersubtext": "", "vitowards": ""}]


def build_plist(python_bin, script_path):
    connections = {}
    objects = []
    uidata = {}
    ypos = 50

    subtext = "Math, units, currency, percentages — result copies to clipboard"
    for kw in ["calc", "="]:
        sf_uid = _uid()
        out_uid = _uid()
        connections[sf_uid] = _connection(out_uid)
        objects.append(_script_filter(sf_uid, kw, "Calculate Anything", subtext, python_bin, script_path))
        objects.append(_clipboard_output(out_uid))
        uidata[sf_uid] = {"xpos": 150, "ypos": ypos}
        uidata[out_uid] = {"xpos": 450, "ypos": ypos}
        ypos += 150

    return {
        "bundleid": "com.github.tchar.calculate-anything.alfred",
        "category": "Productivity",
        "connections": connections,
        "createdby": "tchar",
        "description": "Math, units, currency, percentages — powered by calculate-anything",
        "disabled": False,
        "name": "Calculate Anything",
        "objects": objects,
        "readme": "",
        "uidata": uidata,
        "version": "1.0.0",
        "webaddress": "https://github.com/tchar/ulauncher-albert-calculate-anything",
    }


def main():
    python_bin = str(PYTHON)
    script_path = str(SCRIPT_DIR / "calculate.py")

    if not PYTHON.exists():
        print(f"ERROR: venv not found at {VENV_PATH}")
        print("Create it first:")
        print(f"  python3 -m venv {VENV_PATH}")
        print(f"  {PYTHON} -m pip install 'Pint>=0.17,<=0.23' simpleeval==0.9.13 parsedatetime==2.6 pytz==2021.1")
        raise SystemExit(1)

    WORKFLOW_DIR.mkdir(parents=True, exist_ok=True)

    plist = build_plist(python_bin, script_path)
    plist_path = WORKFLOW_DIR / "info.plist"
    with open(plist_path, "wb") as f:
        plistlib.dump(plist, f)

    icon_src = SCRIPT_DIR.parent / "calculate_anything/images/icon.svg"
    if icon_src.exists():
        shutil.copy2(icon_src, WORKFLOW_DIR / "icon.svg")

    print(f"Installed to: {WORKFLOW_DIR}")
    print()
    print("Usage (Cmd+Space then):")
    print("  calc <expr>   — calculate (math, units, currency, %; copies result)")
    print('  =    <expr>   — same (disable Alfred\'s built-in calculator first)')
    print()
    print("Examples:")
    print("  calc 100 USD to AUD")
    print("  calc 50 km to miles")
    print("  calc 25% of 200")
    print("  calc sin(pi/4)")
    print()
    print("Note: for '=' keyword, go to Alfred Preferences → Features → Calculator")
    print("      and disable the built-in calculator.")


if __name__ == "__main__":
    main()
