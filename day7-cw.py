groceries = ["milk", "bread", "eggs"]

def add_item(item):
    groceries.append(item)

def remove_last_item():
    groceries.pop()

y = lambda x: print(x)

for item in groceries:
    y(f'item: {item}')

def count_characters(items):
    if len(items) == 1:
        return len(items[0])
    return len(items[0]) + count_characters(items[1:])

count = count_characters(groceries)

print(count)