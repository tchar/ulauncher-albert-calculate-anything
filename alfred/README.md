# Calculate Anything — Alfred 5 Integration

This directory adds [Alfred 5](https://www.alfredapp.com/) support to Calculate Anything.

Two keyword tricalcers are created:

| Keyword | Function |
|---------|----------|
| `calc <expr>` | Calculate — result copies to clipboard |
| `= <expr>` | Same (requires disabling Alfred's built-in calculator) |

## Features

All calculate-anything features work through Alfred:

- **Currency**: `calc 100 USD to EUR`, `calc 50 PHP to AUD`
- **Units**: `calc 50 km to miles`, `calc 100 fahrenheit to celsius`
- **Math**: `calc sin(pi/4)`, `calc 2^32`, `calc sqrt(144)`
- **Percentages**: `calc 25% of 200`, `calc 15% + 85`
- **Base N**: `calc hex 255`, `calc bin 42`

## Requirements

- macOS (Alfred 5 is macOS-only)
- Python 3.7+
- Alfred 5 (Powerpack not required for script filters)

## Install

**1. Clone the repo** (if not already done):

```bash
git clone https://github.com/tchar/ulauncher-albert-calculate-anything ~/src/calculate-anything
```

**2. Create a virtual environment** with the required dependencies:

```bash
python3 -m venv ~/.venvs/alfred-calc
~/.venvs/alfred-calc/bin/pip install 'Pint>=0.17,<=0.23' simpleeval==0.9.13 parsedatetime==2.6 pytz==2021.1
```

**3. Run the installer**:

```bash
python3 ~/src/calculate-anything/alfred/install.py
```

This writes `info.plist` into Alfred's workflow directory. Alfred picks it up immediately — no restart needed.

**4. (Optional) Enable currency conversion**

Get a free API key from [fixer.io](https://fixer.io/) and set it as an environment variable in the workflow:

- Open Alfred Preferences → Workflows → Calculate Anything
- Click `[x]` (Environment Variables) in the top-right
- Add `CALCULATE_ANYTHING_FIXER_KEY` = `<your-key>`

On first run with a fresh key the script waits ~3 seconds for the exchange rate cache to populate. Subsequent runs use cached rates (refreshed every 12 hours).

**5. (Optional) Enable the `=` keyword**

Alfred has a built-in calculator that intercepts the `=` keyword. To use it with Calculate Anything instead:

- Open Alfred Preferences → Features → Calculator
- Uncheck "Calculator"

The `calc` keyword works without any changes.

## How It Works

`calculate.py` is an Alfred [Script Filter](https://www.alfredapp.com/help/workflows/inputs/script-filter/). Alfred calls it with the query as `argv[1]` on every keystroke and displays the returned JSON items. Selecting a result copies it to the clipboard via Alfred's clipboard output action.

`install.py` generates `info.plist` (Alfred's workflow definition) and writes it to:

```
~/Library/Application Support/Alfred/Alfred.alfredpreferences/workflows/user.workflow.calculate-anything/
```

The script is referenced by absolute path from `~/src/calculate-anything/alfred/calculate.py` — the repo does not need to be in any special location as long as the path in the plist matches.

## Troubleshooting

**"No result" for everything**: Make sure the venv exists and has the required packages:
```bash
~/.venvs/alfred-calc/bin/python -c "from calculate_anything.query.handlers import MultiHandler; print('OK')"
```

**Currency not working**: Check that `CALCULATE_ANYTHING_FIXER_KEY` is set in the workflow environment variables. Inspect `/tmp/alfred_calc.log` for errors.

**`=` keyword still goes to Alfred's calculator**: Disable it in Alfred Preferences → Features → Calculator.

**Workflow not appearing**: Run `install.py` again, then reload workflows in Alfred Preferences (right-click the workflow → Reload).
