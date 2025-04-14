# ab 是地址(address) 薄(book)的缩写
ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
}

print(f'Swaroop\'s address is {ab["Swaroop"]}')

# 删除一对键值对
del ab['Spammer']

print(f'There are {len(ab)} contacts in the address-book\n')

for name,address in ab.items():
    print(f'Contact {name} at {address}')

# 添加一对键值对
ab['Guido'] = 'guido@python.org'

print(ab)

if 'Guido' in ab:
    print(f"\nGuido's address is {ab['Guido']}")