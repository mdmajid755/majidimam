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

print_lst(fruits)


print(add_item(fruits))


print(combine_lst_elements(fruits))

