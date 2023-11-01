#Data validation
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

#Calculator heading            
print("Python Calculator")

#Get input from user for calculation
def calculate():
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
    loop() 
    
# check if user wants another calculation
def loop():
    choice = input("Do you want to math some more? (Y,N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
    else:
        print("Invalid input!")
        loop()

calculate()