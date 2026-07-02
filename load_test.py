with open("tasks.txt", "w") as file:
    file.write("buy groceries\n")
    file.write("call mom\n")


tasks = []
print("Before loading:", tasks)


try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    print("No file found yet! that's okay")

print("After loading:", tasks)
