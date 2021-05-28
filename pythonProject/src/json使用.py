import json

all_stus = ''' {"xiaowu": { "age": 28, "sex": "男", "name": "小王", "addr": "深圳布吉", "cars": [ "比亚迪唐 DM", "劳斯莱斯", "五菱宏光" ] },"xiaohong": { "age": 18, "sex": "女", "bags": { "qianbao": [ "lv", "七匹狼", "八匹狼" ] },"name": "小红", "addr": "深圳龙华" } }'''
# 将json字符串转为dict
d1 = json.loads(all_stus)
# 将json文件读出来，转换为dict
d2 = json.load(open('test.json', mode='r', encoding='UTF-8'))
print(type(d2))
js1 = json.dumps(d1, ensure_ascii=False)  # 将dict转换为json
js2 = json.dump(d1, open('test1.json', mode='w', encoding='UTF-8'), ensure_ascii=False)
