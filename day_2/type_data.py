# 16进制
print(0xa5)

# e的科学计数法
print(1.05e3)

# list: 可增删元素
list = [1, 3, 5]

# tuple: 不可增删元素
tuple = (1, 3, 5)

# dict: 字典或哈希表
dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

#  set
s = {1, 3, 5}

# 容器操作

# 去掉列表中的一个最小值和一个最大值后，计算剩余元素的平均值
def score_mean(list):
    list.sort()
    list2 = list[1:-1]
    return round((sum(list2)/len(list2)), 1)
list = [9.1, 9.0 ,8.1, 9.7, 19, 8.2, 8.6, 9.8]
print(score_mean(list))

# 打印 99 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d'%(j, i, j * i), end='\t')
    print()

# 样本抽样

from random import randint, sample

list = [randint(0, 50) for _ in range(100)]
print(list)
print(list[:5]) # 取前5个值
list_sample = sample(list, 10) # 取随机10个值
print(list_sample)

# 字符串
# strip 取头尾空格
' I love python\t\n'.strip()
# replace 字符串替换
'i love python'.replace(' ', '_')
# join 合并字符串
'_'.join(['book', 'store', 'count'])
# title 首字母大写
'i love python'.title()
# 返回匹配字符串的起始位置索引
'i love python'.find('python')

# 判断 str1 是否由 str2 旋转而来
def is_rotation(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    
    def is_substring(s1: str, s2: str) -> bool:
        return s1 in s2
    return is_substring(s1, s2 + s2)

r = is_rotation('stringbook', 'bookstring')
print(r)

r = is_rotation('greatman', 'maneatgr')
print(r)

# re 正则
import re
pat = re.compile(r'\w{6, 20}')

pat = re.compile(r'[\da-zA-Z]{6, 20}')

pat.fullmatch('qaz12')
pat.fullmatch('qaz12wsxedcrfvtgb67890942234343434')
pat.fullmatch('qaz_231')

# class 类
class Dog(object):
    def __init__(self, name, dtype):
        self.name = name
        self.dtype = dtype
    def shout(self):
        print('i\'m %s, type: %s' % (self.name, self.dtype))

wangwang = Dog('wangwang', 'cute_type')
print(wangwang.name)
print(wangwang.dtype)
wangwang.shout()

# 私有变量

class Private_Dog(object):
    def __init__(self, name, dtype):
        self.__name = name
        self.__dtype = dtype
    def shout(self):
        print('i\'m %s, type: %s' % (self.__name, self.__dtype))
    def get_name(self):
        return self.__name

# 如何改变某个属性为只读或只写
class Book(object):
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
