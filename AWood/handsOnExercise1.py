def print_list(items):
    for item in items:
        print(item)

def add_to_list(lst):
    lst.append("the function added this")
    return lst

def combine_list_elements(lst):
    return ''.join(lst)

def my_function(*args):
    for arg in args:
        print(arg)

fruits = ["apple", "oranges", "bananas"]

print(fruits[0]) # Output: apple
print(fruits[1]) # Output: oranges
print(fruits[2]) # Output: bananas

result = my_function
print(result)
