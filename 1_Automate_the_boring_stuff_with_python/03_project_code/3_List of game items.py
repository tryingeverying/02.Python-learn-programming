def displayInventury(inventory):
    print('Inventury')
    sum=0
    for item_key,item_value in inventory.items():#遍历字典的key和value时字典后面要加上items()
        print(item_value,item_key)
        sum+=int(item_value)
    print(f'Total number of item:{sum}')

def addToInventury(inventory,addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory

items_list={'glod coin':42,'rope':1}
dragonloot = ['glod coin','dagger','glod coin','glod coin','ruby']
items_list=addToInventury(items_list,dragonloot)
displayInventury(items_list)