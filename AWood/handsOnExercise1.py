def print_lst(items):
    for item in items:
        print(item)

def add_item(my_lst):
    my_lst.append("the function added this")
    return my_lst
    
def combine_lst_elements(my_lst):
    my_string = "".join(my_lst)
    return my_string

fruits = ["apple", "orange", "bananas"]

def fruits():
    return "apple, orange, bananas"

fruit_lst = fruits()
print(fruit_lst)

print(fruits())
