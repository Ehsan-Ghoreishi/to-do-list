# To-Do List

A simple command-line to-do list app written in Python. Tasks are saved locally in a JSON file so they persist between sessions.

## Requirements

- Python 3.7+
- No third-party packages required

## Usage

```bash
python todo.py
```

### Commands

| Command | Description |
|---|---|
| `add <title>` | Add a new task |
| `list` | List all pending tasks |
| `list all` | List all tasks, including completed ones |
| `done <id>` | Mark a task as completed |
| `delete <id>` | Delete a task permanently |
| `help` | Show available commands |
| `quit` | Exit the app |

### Example Session

```
Todo List  (type 'help' for commands)

> add Buy groceries
Added: [1] Buy groceries

> add Read a book
Added: [2] Read a book

> list
  [ ]   1. Buy groceries  (2026-04-26 21:00)
  [ ]   2. Read a book  (2026-04-26 21:00)

> done 1
Completed: Buy groceries

> list all
  [✓]   1. Buy groceries  (2026-04-26 21:00)
  [ ]   2. Read a book  (2026-04-26 21:00)

> delete 1
Deleted task 1.

> quit
Bye!
```

## Data Storage

Tasks are stored in `todos.json` in the same directory as `todo.py`. The file is created automatically on first use and is excluded from version control via `.gitignore`.

## Project Structure

```
to-do-list/
├── todo.py          # Main application
├── todos.json       # Task data (auto-generated, git-ignored)
├── requirements.txt
├── .gitignore
└── README.md
```
