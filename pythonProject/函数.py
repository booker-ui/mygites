def funname(name, a, b):
    print('我是一个函数', name, a, b)


# 当函数中没有return 时,默认返回None


def add_n_m(n, m):
    if m > n:
        return (m - n + 1) * (m + n) / 2  # 返回值
    else:
        print('m需要大于n')


def max(a, b):
    if a > b:
        return a
    else:
        return b


def triangle(a, b, c):
    """
    判断三角形
    :param a: float
    :param b: float
    :param c: float
    :return: None:不是三角形,1:一般三角形,2:等腰三角形,3:等边三角形
    """
    if b + c > a > 0 and a + c > b > 0 and a + b > c > 0:
        if a == b == c:
            return 3
        elif a == b or b == c or a == c:
            return 2
        else:
            return 1
    else:
        return None


tri = triangle(3, 3, 5)


def power(x, n=2, m=1):  # 默认值必须放在最后
    return (x ** n) ** m


num = 257  # 全局


def sum():
    num = 257
    for i in range(100):
        num = num + i
    return num


f = lambda x, y: x ** y  # f 就是函数名

f2 = lambda x, y: x if x > y else y  # 条件成立的时候使用if前的值,条件不成立使用else的值

