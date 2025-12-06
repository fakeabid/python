inventory = []

def add_item(item):
    inventory.append(item)

def count_items(items):
    if len(items) == 1:
        return 1
    return 1 + count_items(items[1:])

show_item = lambda item: print(f"Item in Stock: {item}")

def main():
    add_item('dog food')
    add_item('cat toy')
    add_item('bird cage')
    add_item('fish tank')

    count  = count_items(inventory)

    for item in inventory:
        show_item(item)

    print(count)

main()