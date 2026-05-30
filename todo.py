"""
✅ Todo Manager
A command-line todo list that saves tasks to a JSON file.

Run: python todo.py
"""

import json
import os
from datetime import datetime

DATA_FILE = "todos.json"


def load_todos():
    """Load todos from JSON file. Returns empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_todos(todos):
    """Save todos to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(todos, title):
    """Add a new todo item."""
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Added: [{todo['id']}] {title}")


def list_todos(todos):
    """Display all todos."""
    if not todos:
        print("No todos yet. Add one!")
        return

    print("\n📋  Your Todos:")
    print("-" * 50)
    for t in todos:
        status = "✅" if t['completed'] else "⬜"
        print(f"  {status} [{t['id']}] {t['title']}  ({t['created_at']})")
    print("-" * 50)

    completed = sum(1 for t in todos if t['completed'])
    print(f"Total: {len(todos)} | Done: {completed} | Left: {len(todos) - completed}")


def complete_todo(todos, todo_id):
    """Mark a todo as completed."""
    for t in todos:
        if t['id'] == todo_id:
            t['completed'] = True
            save_todos(todos)
            print(f"✅ Marked as done: [{t['id']}] {t['title']}")
            return
    print(f"❌ Todo #{todo_id} not found.")


def delete_todo(todos, todo_id):
    """Delete a todo by ID."""
    for i, t in enumerate(todos):
        if t['id'] == todo_id:
            removed = todos.pop(i)
            save_todos(todos)
            print(f"🗑️  Deleted: [{removed['id']}] {removed['title']}")
            return
    print(f"❌ Todo #{todo_id} not found.")


def show_help():
    """Show available commands."""
    print("\n📖  Commands:")
    print("  add <task>     — Add a new todo")
    print("  list           — Show all todos")
    print("  done <id>      — Mark todo as completed")
    print("  delete <id>    — Delete a todo")
    print("  help           — Show this help")
    print("  quit           — Exit the program")


def main():
    print("=" * 50)
    print("    ✅  Todo Manager")
    print("=" * 50)

    todos = load_todos()
    print(f"Loaded {len(todos)} todos from storage.\n")
    show_help()

    while True:
        command = input("\n> ").strip()

        if not command:
            continue

        parts = command.split(maxsplit=1)
        action = parts[0].lower()

        if action == "quit":
            print(f"\nSaved {len(todos)} todos. Goodbye! 👋")
            break

        elif action == "add":
            if len(parts) < 2:
                print("Usage: add <task description>")
            else:
                add_todo(todos, parts[1])

        elif action == "list":
            list_todos(todos)

        elif action == "done":
            if len(parts) < 2:
                print("Usage: done <todo id>")
            else:
                try:
                    complete_todo(todos, int(parts[1]))
                except ValueError:
                    print("Please enter a valid todo ID number.")

        elif action == "delete":
            if len(parts) < 2:
                print("Usage: delete <todo id>")
            else:
                try:
                    delete_todo(todos, int(parts[1]))
                except ValueError:
                    print("Please enter a valid todo ID number.")

        elif action == "help":
            show_help()

        else:
            print(f"Unknown command: '{action}'. Type 'help' for commands.")


if __name__ == "__main__":
    main()
