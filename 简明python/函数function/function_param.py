def print_max(a,b):
    if a>b:
        print(f'{a} is maximum')
    elif a == b:
        print(f'{a} is equal to {b}')
    else: 
        print(f'{b} is maximum')

a = int(input("请输入数字a:"))
b = int(input("请输入数字b:"))

print_max(a,b)