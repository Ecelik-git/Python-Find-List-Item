#check if the element in the list
#codingwithec
inventory = ['banana', 'apple', 'pea', 'carrot']
item = input("Enter any item to check: ")
if (item.lower() in inventory):
    print(item + " is currently in the inventory")
else:
    print("We don't have any "+item + " in the inventory yet")
