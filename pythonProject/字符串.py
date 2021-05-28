var1 = '我是一个\n字符串'
var2 = '''我是文档型字符串
你换行我就换行'''
var3 = '开\t,我是表格符号'
print(var1)
print(var3)
# \ 反斜杠是转义字符
# \t 制表符tab  \n 换行 , \' 转义单引号  \\ 转义反斜杠
print('一个反斜杠\'')
# 原始字符串r R
print(r'C:\Program Files\tortoiseGit\bin')
print('C:\Program Files\tortoiseGit\bin')

# 字符串的连接
print('hello' + 'world')
print('hello' + str(8))
print('a' * 5)  # 了解
# 运算
s = R'0123456789'
print('Files' in s)
print('Files' not in s)

# 索引号，从0开始，负数表示倒数第一个
print(s[0], s[1], s[-2])
# 切片
print(s[:])
# 初始化未开始取到 结束位-1
print(s[1:3])
print(s[3:-4])
# 从起始位开始，到结束位，位相距n个取一个
print(s[1:8:2])  # 没隔3取一个
print(s[1::2])
# 面试题
print(s[::-1])
s1 = ' 我是 帅哥！ 是帅哥帅哥 '
# 去除前后空格
print(s1)
val = s1.strip()
print(val)
# 替换
print(s1.replace('是 ', '为'))
# 拆分
val2 = r'C:\Windows\Boot\DVD\EFI\en-US'
val1 = s1.split(' ')
val3 = val2.split('\\')
print(val1)
# 连接
print('/'.join(val3))
# 查找
print(s1.find('帅哥'))

# 先放着
v = val2.encode(encoding='UTF-8')
print(v)

# v1=val2.decode(encoding='UTF-8')
# print(v1)
# 解码字符串，出错默认报ValueError,除非errors是ignore或replace

a = 'abcdefg'
print(a.count('a'))
print(a.index('c'))
print(a[2])
a[2] = '1'
