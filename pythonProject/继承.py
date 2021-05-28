class Circle(object):
    pi = 3.14159

    def __init__(self, r): self.r = r

    def area(self):
        return self.r ** 2 * self.pi


class Cylinder(Circle):
    '''
    创建员类
    '''

    def __init__(self, r, h):
        '''

        :param r: 半径
        :param h: 高度
        '''
        super(Cylinder, self).__init__(r)  # 获取父亲的属性传递过来
        self.h = h

    def area(self):  # 方法重构
        return self.r ** 2 * self.pi * 2 + 2 * self.r * self.pi * self.h

    def volume(self):
        return self.r ** 2 * self.pi * self.h


cl1 = Cylinder(1, 2)
print(cl1.area())
