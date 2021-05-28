l = [0, 1, 2, 3, 4]

ls = iter(l)  # 创建迭代对象，速度快
print(next(ls))  # 访问迭代对象的数据，每访问一次光标下移一位
print(next(ls))
print(next(ls))
print(next(ls))
print(next(ls))

# def ha():
#     l = [0, 1, 2, 3, 4]
#     for i in l: yield i  # 节约内存开销
#
#
# a = ha()
# print(next(a))
# print(next(a))
# print(next(a))
