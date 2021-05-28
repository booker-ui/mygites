# key 必须是不可修改的数据,不能重复,不可以修改
# value 没要求
# 用途 同json 存储结构化的数据
d = {'班级': '项目一',
     '学员信息': [
         {'name': 'Alan',
          'age': 38},
         {'name': 'woodman',
          'age': 18}
     ]}
goods = {'商品类型': '水果',
         '信息': [{'商品名称': '苹果', '价格': 89},
                {'商品名称': '桃子', '价格': 88}]}
# 查
print('商品名称' in goods['信息'][1])
goodname = goods['信息'][1]['商品名称']
g = goods.get('信息')  # 如果无此key返回None
keys = goods.keys()  # 获取所有的键
values = goods.values()  # 获取所有的值
l = len(goods)  # 字典的长度

# 增加 修改
goods['商品类型'] = '果蔬'  # 有相应key
goods['类型'] = '果蔬'  # 无相应key，增加 key：value
# 有相应key,修改value；无相应key，增加 key：value
goods.update({'一级分类': '生鲜', '二级分类': '果蔬', '商品类型': '水果'})
goods['信息'][0].update({'库存': 10})

# 删除
a = goods.pop('类型')  # 指定key删除，返回value
# goods.clear()  # 清空
# print(goods, a)
b = goods.popitem()  # 删除最后一个key:value,放回的是（key,value）


# print(goods, b)



# 复制
d1 = {'woodman': 98, 9.86: 'GM', 'Bobo': [89, 65, 34], 'Mydict': {'Alan': 99}}
d2 = d1  # 浅拷贝
d2['woodman'] = 100
d3 = d1.copy()  # 深拷贝
d3['woodman'] = 5555
print(d1)
print(d2)
print(d3)
d3.pop('woodman')
d3.setdefault('woodman', 1111)
print(d3['woodman'])
