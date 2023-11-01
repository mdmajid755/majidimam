#Define a function that prints out the values in a list that is passed in
def print_shoplist(values):
    for value in values:
        print(value)
#Define a function that adds an item to the list and returns the list
def add_to_shoplist(shoplist, new_item):
    shoplist.append(new_item)
    return shoplist
#Define a function that takes a list argument and returns a string that combines all elements of the list and returns the string
def combine_values(shoplist):
    return ''.join(shoplist)
# Define a list variable that contains the strings apple, oranges, and bananas    
shoplist = ['apples','oranges','bananas']
#Pass the list variable into each function and print out the return values if the function returns a value
print(shoplist)  

print(add_to_shoplist(shoplist, 'the function added this'))

print(combine_values(shoplist))