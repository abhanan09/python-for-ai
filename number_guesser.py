import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break

    if attempts >= max_attempts:
        print(f"Game over! The number was{secret_number}")
        break
