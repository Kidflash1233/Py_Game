# Escape the Rogue AI

Terminal-based adventure where you explore a futuristic campus, gather six cyber tools, and shut down a rogue AI in the Mainframe Core. The project now ships as a modern Python package so it is easy to install, run, and extend.

## Requirements

- Python 3.10 or later
- `pip` for installing the project locally

## Quick start

```bash
git clone https://github.com/Kidflash1233/Py_Game.git
cd Py_Game
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Run the game:

```bash
python -m escape_rogue_ai
```

or use the console script:

```bash
escape-rogue-ai
```

## Gameplay overview

- Move using the numbered options for North/South/East/West exits.
- Collect the six hidden items (Keycard, Laptop, Signal Booster, Ethernet Cable, Debugging Toolkit, Access Codes).
- Once your inventory contains all items, enter the Mainframe Core to win.
- Entering the Mainframe Core early results in a game over.

## Testing

The refactor introduced light unit tests around the core game loop. Run them with:

```bash
pytest
```

## Project layout

```
src/escape_rogue_ai/
├── __init__.py         # Package exports
├── __main__.py         # Entry point for `python -m escape_rogue_ai`
├── data.py             # Static map data and constants
└── game.py             # Game state, menu builder, and CLI loop
tests/
└── test_game.py        # Pytest coverage for the core helpers
```

Extend the map by editing `src/escape_rogue_ai/data.py` and rely on the typed helpers in `game.py` for new flows.
