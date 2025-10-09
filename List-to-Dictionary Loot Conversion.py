# Automate the boring stuff with python
# Chapter 7, Practice Questions
# List-to-Dictionary Loot Conversion

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(str(value) + ' ' + str(key))
        item_total = item_total + value
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] = inv[item] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
