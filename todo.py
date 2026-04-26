import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add_task(title):
    todos = load_todos()
    task = {
        "id": (max((t["id"] for t in todos), default=0) + 1),
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    todos.append(task)
    save_todos(todos)
    print(f"Added: [{task['id']}] {task['title']}")


def list_tasks(show_all=False):
    todos = load_todos()
    filtered = todos if show_all else [t for t in todos if not t["done"]]
    if not filtered:
        print("No tasks found.")
        return
    for t in filtered:
        status = "✓" if t["done"] else " "
        print(f"  [{status}] {t['id']:>3}. {t['title']}  ({t['created_at']})")


def complete_task(task_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == task_id:
            t["done"] = True
            save_todos(todos)
            print(f"Completed: {t['title']}")
            return
    print(f"No task with id {task_id}.")


def delete_task(task_id):
    todos = load_todos()
    remaining = [t for t in todos if t["id"] != task_id]
    if len(remaining) == len(todos):
        print(f"No task with id {task_id}.")
        return
    save_todos(remaining)
    print(f"Deleted task {task_id}.")


def print_help():
    print(
        """
Todo List — Commands:
  add  <title>     Add a new task
  list             List pending tasks
  list all         List all tasks (including completed)
  done <id>        Mark a task as completed
  delete <id>      Delete a task
  help             Show this help message
  quit             Exit
"""
    )


def main():
    print("Todo List  (type 'help' for commands)")
    while True:
        try:
            raw = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not raw:
            continue

        parts = raw.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd == "add":
            if not arg:
                print("Usage: add <title>")
            else:
                add_task(arg)
        elif cmd == "list":
            list_tasks(show_all=(arg.lower() == "all"))
        elif cmd == "done":
            if not arg.isdigit():
                print("Usage: done <id>")
            else:
                complete_task(int(arg))
        elif cmd == "delete":
            if not arg.isdigit():
                print("Usage: delete <id>")
            else:
                delete_task(int(arg))
        elif cmd in ("help", "?"):
            print_help()
        elif cmd in ("quit", "exit", "q"):
            print("Bye!")
            break
        else:
            print(f"Unknown command: '{cmd}'. Type 'help' for available commands.")


if __name__ == "__main__":
    main()
