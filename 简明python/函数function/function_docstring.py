def print_max(x,y):
    '''打印两个数值中的最大数.
    这两个数都应该是整数.'''
    # 如果可能, 将其转换至整数类型
    x = int(x)
    y = int(y)

    if x > y:
        print(f'{x} 最大')
    else:
        print(f'{y}最大')

print_max(3,5)
print(print_max.__doc__)

help(print_max)