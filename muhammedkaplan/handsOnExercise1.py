def printList(list):
    print(list)

def addTheFunctionAddedList(list):
    list.append("the function added this")
    return list

def combin(list):
    return ''.join(list)

fruitList = ["apple", "orange", "bananas"]

printList(fruitList)

addTheFunctionAddedList(fruitList)

printList(fruitList)

printList(combin(fruitList))