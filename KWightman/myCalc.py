#Calculator heading            
print("Python Calculator")

# Declare an empty dictionary to store the results of each calculation
results = {}

# Define a function to perform the calculation and save the result
def calculate():
    # Get the user input for the calculation
    calculation = input("Enter a calculation: ")
    
    # Perform the calculation and save the result
    result = eval(calculation)
    results[calculation] = result
    
    # Print the result
    print(result)
    
    # Return the result
    return result

# Loop through the calculator until the user quits
while True:
    # Get the user input for what they want to do
    action = input("Enter 'c' to calculate, 'h' to view history, or 'q' to quit: ")
    
    # If they want to calculate, call the calculate function
    if action == 'c':
        calculate()
    
    # If they want to view results, print out all of the previous calculations and their results
    elif action == 'h':
        for calculation, result in results.items():
            print(f"{calculation} = {result}")
    
    # If they want to quit, break out of the loop
    elif action == 'q':
        break
    
    # If they enter an invalid option, tell them and ask again
    else:
        print("Invalid option. Please try again.")