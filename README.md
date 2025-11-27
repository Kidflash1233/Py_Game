# Escape the Rogue AI

Terminal-based adventure where you explore a futuristic campus, gather six cyber tools, and shut down a rogue AI in the Mainframe Core. The project now ships as a modern Python package while still including the classic single-file classroom script.

## Highlights
- **Two play styles:** modern CLI entry point (`python -m escape_rogue_ai`) or the original numbered-menu script.
- **Typed, testable code:** rooms and state management now live in `src/escape_rogue_ai/` with light pytest coverage.
- **Beginner friendly:** follow-the-number controls that are perfect for students learning loops and conditionals.
- **Easy distribution:** packaged with `pyproject.toml`, so you can install in editable mode or build wheels.

## Requirements
- Python 3.10+
- `pip` (or `pipx`) for installing dependencies

## Quick start
```bash
git clone https://github.com/Kidflash1233/Py_Game.git
cd Py_Game
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

### Run the packaged game
```bash
python -m escape_rogue_ai
# or
escape-rogue-ai
```

### Run the classic single-file version
```bash
python "Escape the Rogue AI.py"
```
This file matches the original assignment spec and prints the exact numbered menu that the README snippet references.

## Gameplay overview
- Move using the numbered options for North/South/East/West exits.
- Collect all six hidden items:
  | Location | Item |
  | --- | --- |
  | Hallway | Keycard |
  | Computer Lab | Laptop |
  | Rooftop Antenna | Signal Booster |
  | Security Office | Access Codes |
  | Server Room | Debugging Toolkit |
  | Network Closet | Ethernet Cable |
- Once your inventory contains every item, enter the Mainframe Core to win.
- Entering the Mainframe Core early results in an instant game over.

## Development workflow
```bash
# 1. Ensure dependencies are installed (see Quick start)
pytest                # run unit tests
python -m build       # optional: produce sdist/wheel (pip install build if needed)
python -m escape_rogue_ai  # manual smoke test
```
Editing tips:
- Add or reorder rooms via `src/escape_rogue_ai/data.py`.
- Update the CLI behavior in `src/escape_rogue_ai/game.py`.
- Keep new helper modules in `src/escape_rogue_ai/` so imports stay relative and testable.

See `CONTRIBUTING.md` for pull-request guidelines.

## Troubleshooting
- `ModuleNotFoundError: escape_rogue_ai`: run `pip install -e .[dev]` inside your activated virtual environment.
- Script name errors on Windows: wrap the classic filename in quotes (`"Escape the Rogue AI.py"`).
- Text misalignment in terminals: switch to a UTF-8 locale or run via Windows Terminal / VS Code integrated terminal.

## Project layout
```
src/escape_rogue_ai/
├── __init__.py         # Package exports
├── __main__.py         # Entry point for `python -m escape_rogue_ai`
├── data.py             # Static map data and constants
└── game.py             # Game state, menu builder, and CLI loop
Escape the Rogue AI.py  # Original numbered-menu script
tests/
└── test_game.py        # Pytest coverage for the core helpers
```

Extend the map by editing `src/escape_rogue_ai/data.py` and rely on the typed helpers in `game.py` for new flows.

## License
This project is released under the MIT License (see `LICENSE`).

## Contributors
- Kidflash1233 — original creator and maintainer
- davislcruz — gameplay and packaging contributor
