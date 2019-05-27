def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    if not addedItems:  
        return
    else:
        for item in addedItems:
            if item in inventory.keys():
                inventory[item] += 1
            else:
                inventory[item] = 1
    return inventory                

if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    #stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    #displayInventory(stuff)
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)