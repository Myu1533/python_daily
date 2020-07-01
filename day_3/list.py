# 创建list
empty = []
list1 = [1, 'xiaoming', 29.5, '17312662388']
list2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]

# 取长度
len(empty)
len(list1)
len(list2)

# 遍历并输出内置函数type
for _ in list1:
    print(f'{_}的类型为{type(_)}')

# 深拷贝
sku_deep = list2[2].copy()

# copy只拷贝了一层，并不算深拷贝

from copy import deepcopy

a = [1, 2, [3, 4, 5]]
ac = deepcopy(a)
ac[0] = 10
ac[2][1] = 40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1])


# 切片
a = list(range(1, 20, 3)) # range(start, stop, step)
# a[:3] 获取前三个元素
# a[-1] 获取最后一个元素
# a[:-1] 获取除最后一个元素的切片
# a[1:5] 获取[1, 5)切片
# a[1:5:2] 获取[1, 5), 步长为2的切片
# a[::3] 获取[0, len(a)), 步长为3的切片
# a[::-3] 获取[len(a), 0), 步长为3的逆向切片