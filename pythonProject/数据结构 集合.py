# 集合 set 无序 可变
# 定义
s = set()  # 空集合只能用set() 定义
s1 = {1, 1, 2, 4, 'a', 'b', 'ba', 'c'}

# 访问
# 增加
print(s1.add('cd'))
# 删除，随机
print(s1.pop())
s1.remove(4)  # 删除指定的元素
# 长度
print(len(s1))
# 清空
s1.clear()
print(s1)
