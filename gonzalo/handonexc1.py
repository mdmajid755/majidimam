import re

def calculate(expression):
    try:
        return eval(expression)
    except (ZeroDivisionError, SyntaxError):
        return "Error"

def main():
    result = None
    history = []

    while True:
        user_input = input("Enter a mathematical operation (e.g., 1+2, clear, print, reset, or exit): ")

        if user_input == "exit":
            print("Exiting the calculator.")
            break
        elif user_input == "clear":
            result = None
        elif user_input == "reset":
            result = None
            history = []
        elif user_input == "print":
            if history:
                print(" ".join(history))
            else:
                print("No operations to display.")
        else:
            
            if re.match(r'^[0-9+\-*/\s]+$', user_input):
                if result is None:
                    result = user_input
                else:
                    result = str(calculate(result + user_input))

                if result != "Error":
                    history.append(user_input + " = " + result)
                print(f"Result: {result}")
            else:
                print("Invalid input. Please enter a valid mathematical operation.")

if __name__ == "__main__":
    main()
