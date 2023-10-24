
# getting one paramater as value, and loop throuh it
# then print the each item inside of it
def print_list(input_list):
    for item in input_list:
        print(item)

#it takes one paramater, and append it to the new 
# variable that i created on the buttom of the code
def add_to_list(input_list):
    input_list.append("the function added this")
    return input_list

# it takes a argument and with the "join()" method it return it to string.
def combine_list_elements(input_list):
    return ''.join(input_list)

# this is a list variables
my_list = ['apple', 'oranges', 'bananas']


print("Printing the list elements:")
print_list(my_list)

print("\nAdding to the list and returning the modified list:")
# in that way we create new list variable which is contain the "my_list" as well
modified_list = add_to_list(my_list)
print(modified_list)

print("\nCombining list elements into a string:")
combined_string = combine_list_elements(my_list)
print(combined_string)
