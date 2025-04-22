# ex13.py 参数, 解包和变量
from sys import argv
# read the WYSS section for how to run this
script, first, second, third=argv

print(f'The script is called: {script}')
print(f'Your first variable is: {first}')
print(f'Your second variable is :{second}')
print(f'Your third variable is: {third}')