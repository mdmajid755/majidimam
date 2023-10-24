def print_list(items):
    for item in items:
        print(item)

def add_list_item(list, item_to_add):
    list.append(item_to_add)
    return list

def combine_list_items(list):
    return ''.join(list)

test_list = ['test1','test2','test3']
print_list(test_list)

print(add_list_item(test_list, "the function added this"))

print(combine_list_items(test_list))

test_fruits_list = ["apple", "oranges", "bananas"]

print_list(test_fruits_list)

print(add_list_item(test_fruits_list, "the function added this"))

print(combine_list_items(test_fruits_list))