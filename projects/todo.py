tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())

except FileNotFoundError:
    pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Quit")

    choice = input("choose an option")

    if choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        save_tasks()
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            for i, tasks in enumerate(tasks, start=1):
                print(f"{i}, {task}")

            remove_num = int(input("Enter task number to remove! :"))

        try:
            tasks.pop(remove_num - 1)
            save_tasks()
            print("Task removed!")
        except AttributeError:
            print("Invalid task number!")
