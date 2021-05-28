# list 列表 [] 有序  可变(增，删，改)
# tuple 元组 () 有序 不可变
# set  集合 {} 无序 可变 无重复值

l1 = [1, 1, 4, '168', 4, 'Alan', 1]
t1 = ('alan', 12)
s1 = {1, 2, 3, 'alan', 3, 'hello'}
# l1[1] = 'hello'
l2 = [l1, t1, s1]
# 访问
print(l1[1])
# 切片
print(l1[::2])
# 增
l1.append('末尾追加')  # 末尾追加 *****
l1.insert(2, 'insert')  # 指定位置插入，性能慢
# 删除
p = l1.pop()  # 删除末尾，并返回该值 *****
p1 = l1.pop(2)  # 删除指定索引号的值
l1.remove(4)  # 删除指定的遇到的第一个值
# 改
l1[2] = '修改'

# 统计元素有几个
print(l1.count(1))

# 查 第一次遇到值的索引位置
print(l1.index(1))

# 反向
print(l1.reverse())

# 排序
l2 = [4, 5, 1, 3]
l2.sort(reverse=True)  # False 升，True 降

# in not in
print(1 in l2)
print(7 not in l2)

# 长度
print(len(l2))
# 最大，最小值
print(max(l2), min(l2))
# 所有值的和
print(sum(l2))
