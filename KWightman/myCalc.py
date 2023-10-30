#Get input for calculation
#Display results
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def get_op(prompt):
    while True:
        op = input(prompt)
        if len(op) == 1 and op in "+-*/":
            return op
        print("Invalid operator. Please enter +, -, *, or /")
            
print("Python Calculator")

#Format to display in standard output
num1 = get_number("Enter first number: ")
op = get_op("Enter operator (+, -, *, /): ")
num2 = get_number("Enter second number: ")

if op == '+':
    print(num1, "+", num2, "=", (num1 + num2))

elif op == '-':
    print(num1, "-", num2, "=", (num1 - num2))

elif op == '*':
    print(num1, "*", num2, "=", (num1 * num2))

elif op == '/':
    try:
        print(num1, "/", num2, "=", (num1 / num2))
    except ZeroDivisionError:
        print("Cannot divide by zero")
        
# check if user wants another calculation
# break the while loop if answer is no
# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_again = input('Do you want to math some more? Please type Y for YES or N for NO.')

    # If user types Y, run the calculate() function
    if calc_again == 'Y':
        get_number

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
get_number