# Code of Todo-List Manager.  
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    tasks = []
    with open(TASKS_FILE, "r") as file:
        for line in file:
            task_data = line.strip().split(" | ")
            task = {
                "description": task_data[0],
                "priority": task_data[1],
                "completed": task_data[2] == "True",
                "due_date": task_data[3]
            }
            tasks.append(task)
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            task_line = f'{task["description"]} | {task["priority"]} | {task["completed"]} | {task["due_date"]}\n'
            file.write(task_line)

def add_task(description, priority, due_date):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "priority": priority, "completed": False, "due_date": due_date})
    save_tasks(tasks)
    print(f'Task "{description}" added with priority {priority} and due date {due_date}.')

def view_tasks(show_completed=False):
    """View all tasks, optionally showing completed tasks."""
    tasks = load_tasks()
    pending_tasks = [task for task in tasks if not task["completed"]]
    completed_tasks = [task for task in tasks if task["completed"]]

    print("\nPending Tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['description']} [Priority: {task['priority']}, Due: {task['due_date']}]")

    if show_completed:
        print("\nCompleted Tasks:")
        for index, task in enumerate(completed_tasks, start=1):
            print(f"{index}. {task['description']} [Completed, Priority: {task['priority']}]")

def delete_task(index):
    """Delete a task by index."""
    tasks = load_tasks()
    if index <= 0 or index > len(tasks):
        print("Invalid task number.")
    else:
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task["description"]}" deleted.')

def mark_completed(index):
    """Mark a task as completed."""
    tasks = load_tasks()
    if index <= 0 or index > len(tasks):
        print("Invalid task number.")
    else:
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f'Task "{tasks[index - 1]["description"]}" marked as completed.')

def edit_task(index, new_description):
    """Edit an existing task."""
    tasks = load_tasks()
    if index <= 0 or index > len(tasks):
        print("Invalid task number.")
    else:
        tasks[index - 1]["description"] = new_description
        save_tasks(tasks)
        print(f'Task updated to: "{new_description}".')

def view_overdue_tasks():
    """View tasks that are overdue."""
    tasks = load_tasks()
    today = datetime.today().date()

    overdue_tasks = [task for task in tasks if task["due_date"] != "None" and not task["completed"] and datetime.strptime(task["due_date"], "%Y-%m-%d").date() < today]
    
    print("\nOverdue Tasks:")
    if not overdue_tasks:
        print("No overdue tasks.")
    else:
        for index, task in enumerate(overdue_tasks, start=1):
            print(f"{index}. {task['description']} [Due: {task['due_date']}, Priority: {task['priority']}]")

def main():
    """Main function to handle user input."""
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Edit task")
        print("6. View overdue tasks")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            view_tasks(show_completed=True)
        elif choice == '2':
            description = input("Enter a new task description: ")
            priority = input("Enter task priority (High, Medium, Low): ")
            due_date = input("Enter due date (YYYY-MM-DD) or 'None' if not applicable: ")
            add_task(description, priority, due_date)
        elif choice == '3':
            view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                delete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_tasks()
            try:
                task_num = int(input("Enter task number to mark as completed: "))
                mark_completed(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            view_tasks()
            try:
                task_num = int(input("Enter task number to edit: "))
                new_description = input("Enter the new task description: ")
                edit_task(task_num, new_description)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            view_overdue_tasks()
        elif choice == '7':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
