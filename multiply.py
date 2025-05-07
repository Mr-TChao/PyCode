# 计算器

def add(a,b):
    print(f"您选择的计算方式是加法: {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"您选择的计算方式是减法: {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"您选择的计算方式是乘法: {a} * {b}")
    return a * b

def divide(a,b):
    print(f"您选择的计算方式是除法: {a} / {b}")
    return a/b

print("----计算器----")
a = int(input("请输入第一个数字:"))
b = int(input("请输入第二个数字: "))
e = int(input("""
-----计算方式-----
1. 加法
2. 减法
3. 乘法
4. 除法
"""))

if e == 1 :
    print(add(a,b))
elif e == 2:
    print(subtract(a,b))
elif e == 3: 
    print(multiply(a,b))
elif e == 4:
    print(divide(a,b))