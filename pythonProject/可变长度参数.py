def fun1(name, *args):  # *args 任意长度的参数
    print('名字叫', name)
    print('可变参数:', args)


def fun2(name, **kwargs):  # **kwargs 任意长度的参数
    """
    :param name: str 名字
    :param kwargs
        : age: int 年龄
        : h: int 身高
    :return:
    """
    if 'age' in kwargs: kwargs['age'] = 5
    print('名字叫', name)
    print('年龄:', kwargs['age'])
    print('身高', kwargs['h'])


# fun2('Alan', age=39, h=175)
#
# d = {'age': 40, 'h': 180, 'name': "pang"}
# fun2(**d)  # 最常用到的


def add(a, b=2):  # 默认参数值,需要放在最后
    return a + b


def add1(a, b, *args):
    return sum(args) + a + b


def add2(a, b, **kwargs):
    return sum(kwargs.values()) + a + b


print(add1(*[1, 2, 3, 4, 5, 6, 7, 8]))
d = {'a': 1, 'b': 2, '3': 3}
print(add2(**d))
# print(add(1))
# print(add(b=2, a=1))  # 指定参数名传值,无顺序
# t = (1, 2)
# print(add(*t))  # 序列可变传参
# d = {'a': 1, 'b': 2}
# print(add(**d))  # key:value 键值对传参
