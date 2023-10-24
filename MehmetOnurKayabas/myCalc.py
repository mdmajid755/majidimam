def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

result = 0
operations = []

while True:
    print("Options:")
    print("Enter 'add' or '+' for addition")
    print("Enter 'subtract' or '-' for subtraction")
    print("Enter 'multiply' or '*' for multiplication")
    print("Enter 'divide' or '/' for division")
    print("Enter 'print' to display the history of operations and the current result")
    print("Enter 'clear' to reset the result")
    print("Enter 'reset' to restart the calculator with a fresh result and history")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "clear":
        result = 0
        print("Result has been cleared.")
    elif user_input == "reset":
        result = 0
        operations = []
        print("Calculator has been reset with a fresh result and history.")
    elif user_input == "print":
        if not operations:
            print("History is empty.")
        else:
            print("History of operations:")
            for op in operations:
                print(op)
        print("Current result:", result)
    elif user_input in ["add", "subtract", "multiply", "divide","+", "-", "*", "/"]:
        num = float(input("Enter a number: "))
        if user_input == "add" or user_input == "+":
            result = add(result, num)
        elif user_input == "subtract" or user_input == "-":
            result = subtract(result, num)
        elif user_input == "multiply" or user_input == "*":
            result = multiply(result, num)
        elif user_input == "divide" or user_input == "/":
            if num == 0:
                print("Cannot divide by zero")
            else:
                result = divide(result, num)

        operations.append(f" {user_input} {num:.2f} = {result:.2f}")

        print("Result:", result)
    else:
        print("Invalid input. Please try again.")