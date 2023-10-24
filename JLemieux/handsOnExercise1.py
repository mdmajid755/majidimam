fruit_list = ['apples', 'oranges', 'bananas']

def print_list_values(fruit_list):
    for item in fruit_list:
        print(item)

def add_to_list(fruit_list):
    fruit_list.append("the function added this")
    return fruit_list

def combine_list_elements(fruit_list):
    combined_string = ' '.join(fruit_list)
    return combined_string

# Step 1
print("Step 1:")
print_list_values(fruit_list)

# Step 2
print("\nStep 2:")
modified_list = add_to_list(fruit_list)
print(modified_list)

# Step 3
print("\nStep 3:")
combined_string = combine_list_elements(fruit_list)
print(combined_string)