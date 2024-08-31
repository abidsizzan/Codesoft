import os
tasks = []
def display_menu():
    print("\nTo-Do List Application")
    print("a. View Tasks")
    print("b. Add Task")
    print("c. Update Task")
    print("d. Delete Task")
    print("e. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task Number to update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_no - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted Successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
      while True:
        display_menu()
        choice = input("\nEnter your choice (a/b/c/d/e): ")

        if choice == 'a':
            view_tasks()
        elif choice == 'b':
            add_task()
        elif choice == 'c':
            update_task()
        elif choice == 'd':
            delete_task()
        elif choice == 'e':
            print("Exited.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
