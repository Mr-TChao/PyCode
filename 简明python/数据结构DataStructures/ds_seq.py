shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# 索引或下标操作符
print(f'Item 0 is {shoplist[0]}')
print(f'Item -1 is {shoplist[-1]}')
print(f'Character 0 is {name[0]}')

# 切片操作符
print(f'Item 1 to 3 is {shoplist[1:3]}')
print(f'Item 2 to end is {shoplist[2:]}')
print(f'Item 1 to -1 is {shoplist[1:-1]}')
print(f'Item start to end is {shoplist[:]}')

# 步长操作符
print(f'Item start to end with step 2 is {shoplist[::2]}')
print(f'Item start to end with step 3 is {shoplist[::3]}')
print(f'Item start to end with step -1 is {shoplist[::-1]}')