l1 = [1, 1.1, 'hello', 11111, True, None, 1]
# 增加
l1.append('world')
l1.insert(2, '555555')
# 修改
l1[2] = 11111
# 删除
a = l1.pop()  # 删除末尾
b = l1.pop(-2)
l1.remove(11111)  # 删除遇到的第一个值
print(l1, a, b)
# 查
print(l1.index('hello'))

t1 = tuple(l1)
# 集合
s2 = {1.2, 1.1, 'hello'}
s2.add(1.5)
s2.remove(1.1)
c = s2.pop()  # 随机
print(c)
print(s2)
