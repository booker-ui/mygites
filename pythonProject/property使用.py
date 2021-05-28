class Circle(object):
    __pi = 3.14  # 假私有化

    def __init__(self, r):  # 初始化方法
        self.r = r  # 实例属性

    def area(self):
        return self.__pi * self.r ** 2

    @property
    def pi(self):
        return self.__pi



c1 = Circle(1)
c1.pi = 2.15
print(c1.pi)  # 属性的访问
