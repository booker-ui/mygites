# # 判断年龄>=18岁为成年人，30 岁而立只年，60老了
# age = 21
# if 0 > age >= 18:
#     print(age, '岁，你已经是一位成年人')
#     print('你可以找个女朋友了')
# elif 60 >= age > 18:
#     print(age, '岁，而立之年，你结婚了吗？')
# elif age > 60:
#     print(age, '岁，老了')
# else:
#     print(age, '岁，你未成年')
#     print('找个女朋友会被你爸打死')

# 根据年龄 age 判断，是老人，中年人，青年，儿童，婴儿


# 顾客有购买商品list [’苹果‘,’手机‘,'酒']，
# 如果商品中有酒，需要收银员肉眼判断改顾客是否满27周岁，
# 满27直接放行,不满27需要出示证件，
# 判断年龄，如果满18可以购买酒，如果不满18需要回收酒
#
# goods = ['苹果', '手机']
# if '酒' in goods:
#     see_age = int(input('请输入眼观年龄：'))
#     if see_age >= 27:
#         print('放行', goods)
#     else:
#         id_age = int(input('请输入证件年龄：'))
#         if id_age >= 18:
#             print('放行')
#         else:
#             goods.remove('酒')
#             print('放行', goods)
# else:
#     print('放行', goods)

# 三角行
a = float(input('请输入第一条边长：'))
b = float(input('请输入第二条边长：'))
c = float(input('请输入第三条边长：'))

l = [a, b, c]
l.sort()
if 0 < c < a + b and a + c > b > 0 and b + c > a > 0:
    if a == b == c:
        print('等边三角形')
    elif l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        if a == b or b == c or a == c:
            print('等腰直角三角形')
        else:
            print('一般直角三角形')
    else:
        if a == b or b == c or a == c:
            print('等腰三角形')
        else:
            print('一般三角形')
else:
    print('输入错误')
