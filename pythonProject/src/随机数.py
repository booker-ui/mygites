import random

l = ['苹果', '手机', '电脑', '衣服']
ran = random.Random()
print(ran.random())  # 0~1 小数
print(ran.randint(100, 1000))  # 1 到100 的整数
print(ran.choice(l))  # 从序列中随机取值
s = set()
while True:
    s.add(ran.randint(1, 100))
    if len(s) >= 10:
        break
print(s)
