from threading import Thread
import time, random


def func(s):
    print('--开始--', s)
    time.sleep(s)
    print('--结束--', s)


class MyClass(object):
    def func(self, name, sec):
        print('---开始---', name, '时间', time.ctime())
        time.sleep(sec)
        print('***结束***', name, '时间', time.ctime())


# 创建线程
t1 = Thread(target=MyClass().func,args=(3,3))
t2 = Thread(target=func,args=(1,))

# 启动线程
t1.start()
t2.start()
# 等待结束
t1.join()
t2.join()
# ts = []
# for i in range(100):
#     ts.append(Thread(target=func, args=(random.Random().randint(1, 5),)))
#
# for i in ts:
#     i.start()  # 启动
# for i in ts:
#     i.join()  # 等待所有的执行完成


# t1 = Thread(target=MyClass().func, args=(1, 3))
# t2 = Thread(target=MyClass().func, args=(2, 1))
# t1.start()
# t2.start()
# t2.join()
# t1.join()
