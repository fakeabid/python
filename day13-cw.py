# You are helping a small stationery shop owner manage a simple list of items.
# First, ask the user to enter the name of a new item.
# If the file items.txt does not exist, create it and write the item into it.
# If the file exists, open it in append mode and add the new item.
# After writing, display the full list of items from the file to the user

item = input('enter item name: ')

f = open('items.txt', 'a')
f.write(item + '\n')
f.close()

print('\ndisplaying list:')
f = open('items.txt', 'r')
print(f.read())