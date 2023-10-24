# Add
def add(x, y):
    return x + y

# Sub
def sub(x, y):
    return x - y

# Mult
def mult(x, y):
    return x * y

# Div
def div(x, y):
    return x / y

# Create 'operations' list
operations = []

while True: # First loop - program starting

    firstNumber = 0
    secondNumber = 0
    result = 0
    operation = 0

    # Taking first number
    print("---")
    print("'C' for clear")
    print("'R' for reset calculator")
    print("'P' for print previous operations or")
    print("'Q' to exit or")
    print("Enter first number")
    firstNumber = input(": ") # Taking first number
    if firstNumber == "C": # If user wants to clear first number and start again
        continue
    if firstNumber == "P": # If user wants to see previous operations
        print(operations)
        continue
    if firstNumber == "R": # If user wants to reset calculator
        operations.clear()
        continue
    if firstNumber == "Q": # If user wants to exit before enter first number
        print("Exiting...")
        break # Break the first loop
    firstNumber = float(firstNumber) # Convert first number to float
    operations.append(firstNumber) # Adding first number to operations

    while True: # Second loop - running while making operation on result

        # Taking operation
        print("---")
        print("Select an operation:")
        print("'+' or 'add' for add")
        print("'-' or 'sub' for sub")
        print("'*' or 'mult' for mult")
        print("'/' or 'div' for div")
        print("'C' for clear")
        print("'R' for reset calculator")
        print("'P' for print previous operations")
        print("'Q' to exit")
        operation = input(": ") # Taking operation
        if operation == "C": # If user wants start again with protect previous operations
            operations.append("CLEARED")
            break
        if operation == "P": # If user wants to see previous operations
            print(operations)
            continue
        if operation == "R": # If user wants to reset calculator
            operations.clear()
            break # Break second loop
        if operation == "Q": # If user wants to exit before enter operation
            print("Exiting...")
            break # Break second loop
        operations.append(operation) # Adding operation to operations

        # Taking second number
        print("---")
        print("'C' for clear")
        print("'R' for reset calculator")
        print("'Q' to exit or")
        print("Enter second number")
        secondNumber = input(": ") # Taking second number
        if secondNumber == "C": # If user wants start again with protect previous operations
            operations.append("CLEARED")
            break
        if secondNumber == "R": # If user wants to reset calculator
            operations.clear()
            break # Break second loop
        if secondNumber == "Q": # If user wants to exit before enter second number
            print("Exiting...")
            break # Break second loop
        secondNumber = float(secondNumber) # Convert second number to operations
        operations.append(secondNumber) # Adding second number to operations

        # Operations
        if operation == '+' or operation == 'add': # Add operation
            result = add(firstNumber, secondNumber)
        elif operation == '-' or operation == 'sub': # Sub operation
            result = sub(firstNumber, secondNumber)
        elif operation == '*' or operation == 'mult': # Mult operation
            result = mult(firstNumber, secondNumber)
        elif operation == '/' or operation == 'div': # Div operation
            if secondNumber == 0:
                print("---")
                print("Can not divide by 0")
                break
            result = div(firstNumber, secondNumber)

        # Printing Result
        operations.append("=") # Adding = sign to operations
        operations.append(result) # Adding result to operations
        firstNumber = result # Making first number equal to result for use again
        print("---")
        print("Result:", result) # Printing result

    if operation == "Q":
        break # Break first loop when user exit in second loop
    if secondNumber == "Q":
        break # Break first loop when user exit in second loop