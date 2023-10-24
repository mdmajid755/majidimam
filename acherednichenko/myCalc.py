import re

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

last_result = None
operations = []

while True:
    print("type 'clear' for clear")
    print("type 'print' for printing all of the previous operations")
    print("type 'reset' for resetting all of the previous operations")
    print("type 'exit' for exiting cli")
    print("type 'calc' for launching calculator mode")

    user_input = input("Enter operation: ")

    if user_input == 'clear':
        operations.append("clear")
        last_result = None
        print("result is cleared")

    if user_input == 'print':
        operations.append("print")
        print(operations)

    if user_input == 'reset':
        operations.clear()
        last_result = None
        print(operations)

    if user_input == 'exit':
        exit()

    if user_input == 'calc':
        print("Type your expression either *,-,/,+ e.g 1+1, or +1 to use previous result: ")
        operation = input("Type your expression either *,-,/,+ e.g 1+1, or +1 to use previous result:  ")
        # it can be made in a more graceful way but it is interesting to solve it via regular expressions
        pattern = r'(\d*)\s*([\+\-\*/])\s*(\d+)'
        matches = re.findall(pattern, operation)
        # TODO add exception handling
        try:
            for match in matches:
                first_number, operation, second_number = match
                if first_number == '' and last_result is not None:
                    first_number = last_result
                elif first_number == '' and last_result is None:
                    first_number = 0
            if operation == "+":
                result = add(int(first_number), int(second_number))
            if operation == "*":
                result = multiply(int(first_number), int(second_number))
            if operation == "/":
                result = divide(int(first_number), int(second_number))
            if operation == "-":
                result = subtract(int(first_number), int(second_number))
            last_result = result
            operations.append(str(first_number) + operation + str(second_number) + "=" + str(result))
            print(result)
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        finally:
            print("Something went wrong")