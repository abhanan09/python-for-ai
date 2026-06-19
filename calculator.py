while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = input("Choose operation (+,-,*,/): ")

    while operation not in ["+", "-", "*", "/"]:
        operation = input("Invalid Choice. Choose operation ( +,-, *, / )")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Error: Cannot divide by zero"

    print("Result:", result)

    again = input("Calculate Again? (yes/ no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
