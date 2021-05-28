# 1+2...+100
# a = 1  # 起始值
# sum = 0  # 所有数之和
# while a <= 100:
#     sum = sum + a
#     a = a + 1
# print(sum)
# 猜数字，随机给一个100内数，猜他的大小，如大了提示大了，小了提示小了
import random  # 引入随机数

num = random.randint(1, 100)
a = 0
while True:
    guess = input('输入一个整数：')
    guess = int(guess)
    if guess > num:
        print('大了')
    elif guess < num:
        print('小了')
    else:
        print('对了')
    a = a + 1
    if a > 4:
        print('结束')
        break  # 直接结束当前循环
