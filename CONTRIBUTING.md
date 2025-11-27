# Contributing to Escape the Rogue AI

Thanks for taking the time to improve the game! This document outlines the workflow we follow for code, docs, and packaging contributions.

## Getting set up
1. Fork and clone the repository.
2. Create a virtual environment and install the editable package plus dev dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```
3. Install `build` if you plan to produce release artifacts: `pip install build`.

## Development workflow
- Create a feature branch from `main` before making changes.
- Keep code in `src/escape_rogue_ai/` and tests in `tests/`.
- Run the test suite locally:
  ```bash
  pytest
  ```
- For manual verification:
  ```bash
  python -m escape_rogue_ai      # packaged version
  python "Escape the Rogue AI.py"  # classic version
  ```
- Optional: verify packaging succeeds
  ```bash
  python -m build
  ```

## Coding style
- Follow the existing four-space indentation and single-quote style.
- Use descriptive function/variable names; keep helper comments short and purposeful.
- Keep new runtime logic inside the `escape_rogue_ai` package so imports remain relative and testable.

## Submitting pull requests
1. Push your branch and open a PR against `main`.
2. Describe **what** changed and **how** you tested it; screenshots or console logs are encouraged for UX tweaks.
3. Reference any related issues (e.g., `Closes #12`).
4. Be responsive to review feedback—small, focused commits make the process smoother.

Thanks again for helping keep Escape the Rogue AI fun and up to date!
