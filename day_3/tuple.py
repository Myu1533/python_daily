# tuple 元组 immutable
# 创建
a = ()
b = (1, 'xiaoming', 29.5, '17312662388')
c = ('001', '2019-11-11', ['三文鱼', '电烤箱'])

# count
from numpy import random
a = random.randint(1, 5, 10)
at = tuple(a)
at.count(3)