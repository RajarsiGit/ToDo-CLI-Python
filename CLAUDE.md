# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm install        # Install Jest dependencies
npm test           # Run all tests
make test          # Same as npm test
make install       # Same as npm install
make clean         # Remove node_modules
```

To run a single test by name:
```bash
npx jest -t "test name substring"
```

## Architecture

This is a Python CLI todo manager with a Jest (JavaScript) test suite.

- **[todo.py](todo.py)** — All application logic. Reads `sys.argv`, operates on `todo.txt` (pending) and `done.txt` (completed) in the current working directory.
- **[todo.sh](todo.sh)** / **[todo.bat](todo.bat)** — Thin shell wrappers that invoke `python todo.py`. The tests call `todo.sh` directly via `execSync`.
- **[todo.test.js](todo.test.js)** — 20 Jest tests covering all commands. Tests invoke the CLI as a subprocess and assert on stdout.

## Data format

`todo.txt` — one task per line, plain text.  
`done.txt` — completed tasks, one per line, prefixed with `x YYYY-MM-DD `.

## Commands implemented

| Command | Behavior |
|---|---|
| `help` | Print usage |
| `add "text"` | Append to `todo.txt` |
| `ls` | List pending todos in reverse order (newest last added = #1) |
| `del N` | Remove line N from `todo.txt` |
| `done N` | Move line N from `todo.txt` to `done.txt` with today's date |
| `report` | Print count of pending and completed todos |

## Testing notes

Tests use `execSync` with `{cwd: "/tmp"}` so the app reads/writes `/tmp/todo.txt` and `/tmp/done.txt`. Each test cleans up these files. The test suite is the source of truth for expected output strings.
