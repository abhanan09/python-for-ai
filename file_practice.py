tasks = ["buy milk", "walk dog", "finish homework"]

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

loaded_tasks = []

with open("tasks.txt", "r") as file:
    for line in file:
        loaded_tasks.append(line.strip())

print(loaded_tasks)
