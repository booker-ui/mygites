from configparser import ConfigParser

config = ConfigParser()  # 创建一个对象
config.read('test1.ini', encoding='UTF-8')
# 获取lang下name的值，不存在抛出KeyError异常
print('lang>name:', config['lang']['name'])
if 'lang' in config and 'name' in config['lang']:
    name = config['lang']['name']
# 获取整个menu块的值
menu = config['menu']
# 获取menu块下的officialSite的值
print('menu>officialSite:', menu['officialSite'])
# 判断配置文件中是否存在menu块
print('menu' in config)
print('officialSite' in menu)
# 得到所有的section
print('sections:', config.sections())
# 得到该menu的所有option选项，不存在NoSectionError异常
print('options:', config.options('menu'))
# 得到该menu的所有键值对，不存在NoSectionError异常
print('items:', config.items('menu'))
for key, value in config.items('menu'):
    print(key, value)
# 得到menu中service的值，返回为string类型，不存在NoSectionError或NoOptionError异常
print('menu>service(str):', config.get('menu', 'service'))
# 得到 menu 中 id 的值，返回为 int 类型
print('menu>id(int):', config.getint('menu', 'id'))
# 用法比较灵活
print('menu>id(int):', config['menu'].getint('id'))
# config.add_section('menu1')
config['menu1']['option'] = '5555'
config.write(open('test1.ini', "w",encoding='UTF-8'))
