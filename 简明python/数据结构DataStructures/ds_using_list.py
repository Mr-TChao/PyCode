# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(f'i have {len(shoplist)} items to purchase.')

print(f'These items are:', end=' ')

for iteam in shoplist:
    print(iteam, end=' ')

print('\nAlso, we have to buy rice.')
shoplist.append('rice')
print(f'My shopping list is now {shoplist}')

print(f'I will sort my list now')
shoplist.sort()
print(f'Sorted shopping list is {shoplist}')


print(f'The first item I will buy is {shoplist[0]}')
olditem = shoplist[0]
del shoplist[0]
print(f'I bought the {olditem}')
print(f'My shopping list is now {shoplist}')