list1 = [0, 1, 18, 9, 7, 17, 12, 6]


def fun(x):
    return x % 2 == 0


# f1 = filter(fun, list1)  # 第一个参数使用的是函数名
# filter依次从序列中取出数据,符合函数结果的返回,不符合的去除
# f2 = filter(lambda x: x % 2 == 0, list1)
# f3 = filter(lambda x: x is not None, list1)
f3 = filter(lambda x: True if x is not None else False, list1)

# print(list(f1))
# print(list(f2))

l1 = list(f3)
print(l1)
f4 = map(lambda x: x * 2, l1)  # 映射处理,取序列中的值进行处理
print(list(f4))
print(sum(list1))
