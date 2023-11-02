# Initialize variables
current_value = None
operations = []

# Function to perform calculation based on operator and user_input_num
def calculate(operator, user_input_num, current_value):
    if operator == '+':
        return current_value + user_input_num
    elif operator == '-':
        return current_value - user_input_num
    elif operator == '*':
        return current_value * user_input_num
    elif operator == '/':
        if user_input_num != 0:
            return current_value / user_input_num
        else:
            print("Error: Division by zero")
            return current_value

# While loop
while True:
    user_input = input("Enter your command: ")

    # Clear command
    if user_input == 'clear':
        current_value = None

    # Print command
    elif user_input == 'print':
        print(" ".join(operations))

    # Reset command
    elif user_input == 'reset':
        current_value = None
        operations = []

    # Exit command
    elif user_input == 'exit':
        break

    # If it's a mathematical operation
    else:
        if current_value is None:
            try:
                current_value = eval(user_input)
                operations.append(user_input + ' = ' + str(current_value))
            except:
                print("Invalid input. Please try again.")
        else:
            try:
                operator, user_input_num = user_input.split()[0], eval(user_input.split()[1])
                current_value = calculate(operator, user_input_num, current_value)
                operations.append(user_input + ' = ' + str(current_value))
            except:
                print("Invalid input. Please try again.")
