#  我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项
# 明了胜过晦涩, 显式优于隐式

from hmac import new
from types import new_class


zoo =('python', 'elephant', 'penguin')
print(f'Number of animals in the zoo is {len(zoo)}')


new_zoo =  'monkey', 'camel', zoo
print(f'Number of cages in the new zoo is {len(new_zoo)}')
print(f'All animals in new zoo are', new_zoo)
print(f'Animals brought from old zoo are', new_zoo[2])
print(f'Last animal brought from old zoo is', new_zoo[2][2])
print(f'Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))