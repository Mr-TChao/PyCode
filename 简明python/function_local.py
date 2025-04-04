x = 50
def func(x):
    print(f'{x} is x')
    x = 2
    print(f'changed local x to {x}')

func(x)
