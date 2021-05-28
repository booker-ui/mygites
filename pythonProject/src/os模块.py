import os

path = '.'
print(os.getcwd())  # 当前执行文件所在的目录
# os.chdir(r'C:/')
# print(os.getcwd())
l=[]
for root, dirs, files in os.walk(r'F:\pythonProject'):
    print('root:', root)
    print('dir', dirs)
    print('file', files)

print(os.path.abspath('.'))

# 获取当前项目的路径
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("InfoServiceSystem\\") + len("InfoServiceSystem\\")]
path = os.path.abspath(rootPath + r'/com/gif/1.gif')

print(os.path.basename(r'F:\pythonProject\src\os模块.py'))  # 获取路径中的文件名
print(os.path.dirname(r'F:\pythonProject\src\os模块.py'))  # 获取路径中的目录

print(os.path.exists(r'F:\pythonProject\sr'))  # 目录是否存在
print(os.path.getsize(r'F:\pythonProject\src\os模块.py'))

# 12、用python语言写一个查找给定文件夹下面的所有文件，
# 并输出文件大小大于10G的文件名（现场写一个可以执行的demo）


