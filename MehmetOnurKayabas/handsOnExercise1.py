def define_list(inputlist):
    print(inputlist)
def add_string(inputlist):
    inputlist.append("the function added this")
    return inputlist
def combine_all(inputlist):
    combined =''.join(inputlist)
    return combined
fruits=["Apples","Oranges","Bananas"]
define_list(fruits)
add_string(fruits)
define_list(fruits)
define_list(combine_all(fruits))