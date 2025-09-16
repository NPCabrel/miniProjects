#Store tasks in a list.

#Allow the user to: add a task, view all tasks, or remove one.

#(Bonus: save the list into a file and load it again when the program runs.)

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')


def remove_task():
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to remove.")

def main():
    while True:
        print("\nOptions:")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
# I added a while loop to allow continuous task management until the user decides to exit.
# I added functions to organize the code better and improve readability.

