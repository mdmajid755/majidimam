#Print shopping list
shoplist = ['apples','oranges','bananas']
print("\nShopping List:\n")
print(','.join(map(str, shoplist)))
#Add to shopping list and print
shoplist.append("the function added this")
print("\nShopping List:\n")
print(','.join(map(str, shoplist)))