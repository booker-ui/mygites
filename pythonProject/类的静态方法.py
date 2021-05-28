class Date(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        if '-' in date_as_string:
            s = '-'
        elif '/' in date_as_string:
            s = '/'
        year, month, day = date_as_string.split(s)
        date = cls(year, month, day)  # 实例化
        return date

    @staticmethod
    def is_date_valid(date_as_string):
        if '-' in date_as_string:
            s = '-'
        elif '/' in date_as_string:
            s = '/'
        year, month, day = date_as_string.split(s)
        return int(year) <= 2100 and int(month) <= 12 and int(day) <= 31


# 静态方法中没有cls 类，相当于一个函数
print(Date.is_date_valid('2212/12/31'))
# 可以在外部不创建实例访问
data3 = Date.from_string('2012/12/31')
print(data3.year)
