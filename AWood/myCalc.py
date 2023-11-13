import tkinter as tk

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

window = tk.Tk()
window.title('Hello Calckies!')

window.mainloop()

print("donezo")

buttonGridFrame = tk.Frame(master=window)

# Define a function to add two numbers
def add(x, y):
  return x + y

# Define a function to subtract two numbers
def subtract(x, y):
  return x - y

# Define a function to multiply two numbers
def multiply(x, y):
  return x * y

# Define a function to divide two numbers
def divide(x, y):
  return x / y

# Ask the user to choose an operation

# Define history funcion

history = ()

print("Please choose an operation:")

print("1. Add")

print("2. Subtract")

print("3. Multiply")

print("4. Divide")

print("5. Show hisotry plz")

print("6. End")

choice = input("Enter your choice (1/2/3/4/5): ")
if choice == "6":
   print("Many thanks for using Calcy! Have a Cake-tastic day :P")

if choice == "5":
   print("The operation history is:")
   print(history)

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))
if choice == '1':
  print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
  print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
  print(num1, "/", num2, "=", divide(num1, num2))

else:
  print("Invalid input")

