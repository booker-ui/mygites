# l = set((1, 2, 3, 4, 5, 1, 2, 3))
# for i in l:
#     print(i)

# d = {'woodman': 98, 'Alan': 89, 'Bobo': 56}
# for i in d:  # 数据量小的时候用
#     print(d[i])
#
# for key, value in d.items():  # 数据量大的时候用
#     print(key, value)

# print(list(range(5)))  # [0, 1, 2, 3, 4]
# print(list(range(1, 5)))  # [1, 2, 3, 4]
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
# sum = 0
# for i in range(1, 100, 2):  # 奇数之和
#     sum = sum + i
# print(sum)
# 九九乘法表
# for i in range(1, 10):  # 控制输出行数
#     a = i + 1
#     for j in range(1, a):  # 控制每行的个数
#         print('{j}*{i}={k}'.format(i=i, j=j, k=i * j), end='\t')
#     print('')
# 冒泡排序
l = [9, 2, 7, 4, 5, 6, 3, 8, 1, 10]
lengt = len(l)
for i in range(lengt):
    for j in range(i + 1, lengt):
        if l[i] > l[j]:
            l[j], l[i] = l[i], l[j]

print(l)
