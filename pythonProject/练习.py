# 练习2：有一个字典
# {'key1': '123456', 'key2': [1, 2, 3, 5, 6, 8], 'k3': '345'},
# 检查传入的每个key的值长度，如果长度大于2的话，保留前两个长度的内容，并将新内容返回给调用者。

# def fun(d: dict):
#     d1 = {}
#     for key, value in d.items():
#         if len(value) >= 2:
#             d1[key] = value[:2]
#         else:
#             d1[key] = value
#     return d1
#
#
# d = {'key1': '123456', 'key2': [1, 2, 3, 5, 6, 8], 'k3': '34'}
# print(fun(d))


# 练习3：定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)
# ---- {每科成绩对应的数据类型为字典，如：{"语文":85,"数学":90,"英语":65}}
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高分的科目名和对应的分数。get_course()

class Student(object):
    def __init__(self, name, age, **score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def max_score(self):
         return {key: value for key, value in self.score.items() if value == max(self.score.values())}

    def m_score(self):
        d = {}
        for key, value in self.score.items():
            if value == max(self.score.values()):
                d.update({key: value})
        return d


s1 = Student('Alan', 39, **{'Ch': 15, 'Math': 120, 'En': 120})
print(s1.max_score())
print(s1.m_score())
