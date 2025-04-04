x = 50
def func():
    global x
    print(f'x is {x}')
    x = 2
    print(f'changed global x to {x}')


func()
print(x)