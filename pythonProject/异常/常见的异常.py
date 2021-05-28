def add(a, b):
    assert 1 + a > 10, '计算结果错误'
    return a * b


l = [1, 2, 3]


# TypeError  参数类型错误
# IndexError 索引号异常
# AssertionError 断言的异常
# IOError  IO异常，打开文件不存在，无权限访问
# ImportError & ModuleNotFoundError 模块不存在

def aaa(a):
    add(a, 2)


# AssertionError
try:
    # a=1/0
    fo1 = open('1111', 'r', encoding='utf-8')
    print(fo1.read())
except FileNotFoundError as e:
    print(e)
    print('出现异常了')
except ZeroDivisionError as e:
    print(e)
    print('1/0异常')
except (IndexError, IOError) as e:
    pass
finally:  # 释放资源
    print('不管是否出现，都运行')
    print('收尾')
    fo1.close()
