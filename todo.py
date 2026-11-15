"""Simple command-line to-do list."""

tasks = []


def add_task(title):
    """Add a new task to the list."""
    tasks.append({"title": title, "done": False})


def show_tasks():
    """Print all tasks with their status."""
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")


def complete_task(number):
    """Mark a task as done."""
    tasks[number - 1]["done"] = True


def main():
    while True:
        print("\n1) Add  2) Show  3) Complete  4) Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_task(input("Task: "))
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            complete_task(int(input("Task number: ")))
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
