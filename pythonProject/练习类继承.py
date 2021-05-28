class Animal(object):  # 基类、父类

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def call(self):
        print('叫')

    def dance(self):
        pass


class Rewu(object):

    def __init__(self, name, sex, wuqi, yifu, fy, gj):
        self.name = name
        self.sex = sex
        self.wuqi = wuqi
        self.yifu = yifu
        self.fy = fy
        self.gj = gj

    def pingA(self):
        pass

    def jineng(self):
        pass


class Cat(Animal):

    def __init__(self, name, sex, age, height):
        super(Cat, self).__init__(name, sex)
        self.age = age
        self.height = height

    def call(self):
        print(self.name, '喵喵')

    def dance(self):
        print('猫舞步')

    def eat(self):
        print('一口一条鱼')


class Dog(Animal):

    def __init__(self, name, sex, age, height):
        super(Dog, self).__init__(name, sex)
        self.age = age
        self.height = height

    def call(self):
        print(self.name, '旺旺')


animal = Animal('小黑', '男')
mimi = Cat('Mimi', '女', 3, height=35)
ww = Dog('Wanwan', '男', 8, height=46)


def do(A):
    A.call()


class Student(object):

    def __init__(self, name, age, **score: dict):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def max_mark(self):
        return {key: value for key, value in self.score.items() if value == max(self.score.values())}
stu=Student('Alan',18,**{"语文":90,"数学":90,"英语":65})
print(stu.max_mark())