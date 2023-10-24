def plus(a,b):
    print(a + b)

def minus(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)
    
def divide(a,b):
    print(a/b)

savedOperations = []

while True:

    print("Welcome")
    print("P for last operations")
    print("write E for exit")
    firstNumber = input("write the first number")
    if firstNumber == "E":
        break
    if firstNumber == "P":
        print(savedOperations)
        continue
    savedOperations.append(firstNumber)
    print(" you wrote " + firstNumber +  " for the first number ")
    firstNumber = float(firstNumber)
   
    while True:

        print("write E for exit")
        print("P for last operations")
        print("+ or add or - or sub or / div or * or mult")
        operation = input ("write the operation")
        print(" you wrote " +  operation)
        print("write E for exit")
        print("P for last operations")
        if operation == "E":
            break
        if operation == "P":
            print(savedOperations)
            continue

        savedOperations.append(operation)

        secondNumber = input("write the second number ")
        print(" you wrote " + secondNumber + " for the second number ")
        secondNumber = float(secondNumber)
        if secondNumber == "E":
            break
        if secondNumber == "P":
            print(savedOperations)
            continue
        savedOperations.append(secondNumber)

        if operation == "+" or operation == "add":
            result =  firstNumber + secondNumber
            savedOperations.append("=")
            savedOperations.append(result)
            plus(firstNumber, secondNumber)
        elif operation == "-" or operation == "sub":
            result =  firstNumber - secondNumber
            savedOperations.append("=")
            savedOperations.append(result)
            minus(firstNumber, secondNumber)
        elif operation == "*" or operation == "mult":
            result =  firstNumber * secondNumber
            savedOperations.append("=")
            savedOperations.append(result)
            multiply(firstNumber, secondNumber)
        elif operation == "/" or operation == "div":
            result =  firstNumber / secondNumber
            savedOperations.append("=")
            savedOperations.append(result)
            divide(firstNumber, secondNumber)
        else:
            print("no exist")
        print("Would you like to continue with this number")
        contunieOrNot = input("Y/N? :")
        if contunieOrNot == "Y":
            firstNumber = result
        elif contunieOrNot =="N":
            break
            