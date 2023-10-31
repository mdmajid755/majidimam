# Define a function that prints out the values in a list that is passed in
def printValues(list):
    print(list)

# Define a function that takes a list argument and adds “the function added this” to the list and returns the list
def addStringToList(list):
    list.append("the function added this")
    return list

# Define a function that takes a list argument and returns a string that combines all elements of the list and returns the string
def combineListElements(list):
    return (''.join(list))

# Define a list variable that contains the strings apple, oranges, and bananas

fruits = ['apple', 'orange', 'bananas']

# Pass the list variable into each function and print out the return values if the function returns a value

# ['apple', 'orange', 'bananas']
printValues(fruits)

# ['apple', 'orange', 'bananas', 'the function added this']
print(addStringToList(fruits))

# appleorangebananasthe function added this
print(combineListElements(fruits))