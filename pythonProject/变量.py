# 单行注释

# 存储数据

# 右连接性
a, b = 5, 2
# python 变量，动态变量,变量可以赋值任何类型的数据
# 取模，获得余数
c = a % b  # 1
# 幂,a的b次方
c = a ** b  # 25
# 取整，取除后的整数
c = a // b  # 2
print(c)

print(not a != b)
# and 两端未 True 是才为True
# or 只要有一个为True，那他就是True
print(a < b or b < 1)
print(b > 1 or a ** 2 > b ** 5 and a / 2 * b + 1 < 5)

# 1、让用户从键盘输入两个数字，然后计算出他们的和
a1 = float(input("请输入数字："))  # str 字符1串
a2 = float(input("请输入数字："))
print(a1 + a2)
# 2、如何输出保留小数点后两位的数据？ --> 使用 print('%.2f'%变量)，如：print('%.2f'%b)
