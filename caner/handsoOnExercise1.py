def listeyiYazdir(list):
    print(list)

def addThefunctionAddedThis(list):
    list.append("the function added this")
    return list

def icerikleriBirlestir(list):
    return ''.join(list)

listA = ["apple","oranges","bananas"]

listeyiYazdir(listA)

addThefunctionAddedThis(listA)
listeyiYazdir(listA)

listeyiYazdir(icerikleriBirlestir(listA))
