tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Quit")

    choice = input("choose an option")

    if choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
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
            print("Task removed!")
        except AttributeError:
            print("Invalid task number!")
