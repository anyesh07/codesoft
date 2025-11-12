
import json
import os
from datetime import datetime

DATA_FILE = "todo_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    title = input("Title: ").strip()
    if not title:
        print("Empty title. Cancelled.")
        return
    tasks.append({
        "id": int(datetime.utcnow().timestamp() * 1000),
        "title": title,
        "done": False,
        "created_at": datetime.utcnow().isoformat()
    })
    save_tasks(tasks)
    print("Added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "✓" if t.get("done") else " "
        print(f"[{status}] {t['id']} - {t['title']}")

def toggle_done(tasks):
    list_tasks(tasks)
    try:
        tid = int(input("Enter task id to toggle done: ").strip())
    except:
        print("Invalid id.")
        return
    for t in tasks:
        if t["id"] == tid:
            t["done"] = not t.get("done", False)
            save_tasks(tasks)
            print("Toggled.")
            return
    print("Not found.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        tid = int(input("Enter task id to delete: ").strip())
    except:
        print("Invalid id.")
        return tasks
    new = [t for t in tasks if t["id"] != tid]
    if len(new) == len(tasks):
        print("Not found.")
    else:
        save_tasks(new)
        print("Deleted.")
    return new

def menu():
    while True:
        tasks = load_tasks()
        print("\n1) Add  2) List  3) Toggle Done  4) Delete  5) Exit")
        choice = input("> ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            toggle_done(tasks)
        elif choice == "4":
            _ = delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Unknown choice.")

if __name__ == "__main__":
    menu()
