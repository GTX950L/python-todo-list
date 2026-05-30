# ✅ Todo Manager

A command-line todo list app built with Python.  
Tasks are saved to a JSON file so they persist between sessions.

## 🚀 How to Run

```bash
python todo.py
```

## 📖 Usage

```
> add Buy groceries
✅ Added: [1] Buy groceries

> add Finish Python homework
✅ Added: [2] Finish Python homework

> list
📋  Your Todos:
  ⬜ [1] Buy groceries  (2026-05-30 19:00)
  ⬜ [2] Finish Python homework  (2026-05-30 19:01)
Total: 2 | Done: 0 | Left: 2

> done 1
✅ Marked as done: [1] Buy groceries

> delete 2
🗑️  Deleted: [2] Finish Python homework

> quit
Saved 1 todos. Goodbye! 👋
```

## 🛠️ Features

- ✅ Add new tasks
- ✅ List all tasks with status
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ Data persists to `todos.json`
- ✅ Progress summary (done vs total)

## 📚 What I Learned

- Working with JSON files (`json.load`, `json.dump`)
- Date/time formatting (`datetime`)
- File existence checking (`os.path.exists`)
- List comprehensions
- Dictionary data structures
- Interactive command parsing
