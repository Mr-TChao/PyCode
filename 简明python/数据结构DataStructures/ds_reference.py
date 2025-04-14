print('Simple Assingnment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist 

del shoplist[0 ]
print(f'shoplist {shoplist}')
print(f'mylist {mylist}')

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print(f'shoplist {shoplist}')
print(f'mylist {mylist}')

