# 这是一个字符串对象
from operator import delitem

from 简明python.数据结构DataStructures.ds_reference import mylist


name = 'Swaroop'

if name.startswith('Swa'):
    print(f'Yes, the string {name} starts with "Swa"')

if a in name:
    print(f'Yes, the string {name} contains the string "a"')

if name.find('war') != -1:
    print(f'Yes, the string {name} contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))