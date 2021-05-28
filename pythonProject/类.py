class Circle(object):
    pi = 3.14  # 假私有化

    def __init__(self, r):  # 初始化方法
        self.r = r  # 实例属性

    def area(self):
        assert Circle.pi == self.pi, '数字被修改'
        return self.pi * self.r ** 2


c1 = Circle(1)
c1.pi=3
print(c1.area())


class Cuboid(object):

    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h
