import json
import os

DB_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DB_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n--- Current Tasks ---")
    for i, t in enumerate(tasks, 1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\nCommands: (1) Add  (2) List  (3) Complete  (4) Delete  (5) Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            title = input("Enter task description: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice in ("3", "4"):
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number: ")) - 1
                if 0 <= idx < len(tasks):
                    if choice == "3":
                        tasks[idx]["done"] = True
                        print("Task marked as completed.")
                    else:
                        removed = tasks.pop(idx)
                        print(f"Removed: {removed['title']}")
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
