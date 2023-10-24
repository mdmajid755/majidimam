def add(a, b):
    print (a + b)

def subtraction(a, b):
    print (a - b)

def division(a, b):
    print (a / b)

def multiple(a, b):
    print (a * b)

saved = []

while True: 

    print("Hi")
    print("to see previus transactions 'P' ")
    print("type E to exit or ")
    firstNumber = input("firstNumber: ")
    if firstNumber == "E":
        break
    if firstNumber == "P":
        print(saved)
        continue
    saved.append(firstNumber)
    print("firstNumber " + firstNumber + " typed")
    firstNumber = float(firstNumber)

    while True:

        print("+ or add or - or sub or / or div or * or mult")
        print("to see previus transactions 'P' ")
        print("type E to exit or ")
        operation = input("operation: ")
        if operation == "E":
            break
        if operation == "P":
            print(saved)
            continue
        saved.append(operation)
        print(operation + " you would like to do")

        print("type E to exit or ")
        print("to see previus transactions 'P' ")
        secondNumber = input("second Number: ")
        if secondNumber == "E":
            break
        if secondNumber == "P":
            print(saved)
            continue
        saved.append(secondNumber)
        print("secondNumber " + secondNumber + " typed")
        secondNumber = float(secondNumber)

        if operation == '+' or operation == 'add':
            result = firstNumber + secondNumber
            saved.append("=")
            saved.append(result)
            add(firstNumber,secondNumber)
        elif operation == '-' or operation == 'sub':
            result = firstNumber - secondNumber
            saved.append("=")
            saved.append(result)
            subtraction(firstNumber,secondNumber)
        elif operation == '/' or operation == 'div':
            result = firstNumber / secondNumber
            saved.append("=")
            saved.append(result)
            division(firstNumber,secondNumber)
        elif operation == '*' or operation == 'mult':
            result = firstNumber * secondNumber
            saved.append("=")
            saved.append(result)
            multiple(firstNumber,secondNumber)
        else:
            print("operation not found")

        print("to continue?")
        continueoption = input("Y/N?: ")

        if continueoption == "Y":
            firstNumber = result
        elif continueoption == "N":
            break