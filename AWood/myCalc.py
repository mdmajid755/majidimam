def clear():
    global input # Use the global variable input
    input = None # Set input to None
    return input # Return input

operations = []

def print_operations():
    global operations
    if not operations:
        print("No operations have been input to the calculator.")
    else:
        print("The operations input to the calculator are:")
        for operation in operations:
            print(operation)

def reset():
    global operations
    global input
    operations = []
    input = None
    print("The calculator has been reset")

running = True

def exit():
    global running
    running = False
    print("The program has been exited.")

history = ()

history = history + ("",)

print(history)