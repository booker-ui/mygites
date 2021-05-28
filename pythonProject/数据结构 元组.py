# tuple 有序 不可变 ()
t1 = (1,)  # 定义一个元素时
t2 = (1, 2, 3, 1, 4)

# 访问
print(t2[2])

# 查
print(t2.index(2))

# 统计
print(t2.count(1))

# 元素是否存在
print('abc' in t2)
print('2' not in t2)

print(t2)

# 长度
print(len(t2))
# 所有值的和
print(sum(t2))
# 最大，最小值
print(max(t2), min(t2))
