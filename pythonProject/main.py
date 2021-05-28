# end 参数控制输出时最后的结束
print(1, 2, 3, end=' ')
print(1, 2, 3)
s = '我是%s,今年是%s' % ('alan', 2021)
print(s)
s1 = '{name}：{site}'.format(name='知乎', site='www.zhihu.com')
print(s1)
# input1 = input('从键盘接收数据：')
# print(input1)
sss_1 = None
# 赋值右连接性
a = b = c = 1
t = ['a', 'b', 'c']
a = 'abc'
b = ''.join(t)
print(a, b)
# 比较值是否相等
print(a == b)
print(id(a))
print(id(b))
# 值、类型、地址空间
print(a is b)
a = 12355555655665655616666161616516516161616165165356464651461616161613516516165161651651365160
print(type(a))
c = None
print(id(c))
s = r'C:\Windows\boot\DVD\EFI\en-US'
print(s[1:10:2])
print(s[::-1])
s.strip()  # 去前后空格
print(s.split('\\'))  # 切割
print(s.replace('\\', '/'))  # 替换
print(s.find('DVD'))  # 查找出字符串索引号的起始位置
list1 = [1, 2]
print(list1[0], list1[-1])
list1.append('abc')  # 追加 *****
list1.append('bcd')
list1.pop()  # 删除末尾 *****
list1.pop(1)  # 删除指定索引值 ***
list1.remove('abc')  # 删除遇到的第一值 # ***
print(list1)
# tuple 有序，不可变
tuple1 = ('C:', 'Windows', 'boot', 'DVD', 'EFI', 'en-US')
print(tuple1.count('DVD'))
print(tuple1.index('DVD'))
print(tuple1)
# 无序，可变
set1 = {'C:', 'Windows', 'boot', 'DVD', 'EFI', 'en-US'}
# 增加
set1.add('Windows')
# 删除 随机
set1.pop()
# 删除指定值
set1.remove('boot')
set1.clear()  # 清空
print(set1)
