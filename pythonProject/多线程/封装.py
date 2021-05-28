from threading import Thread
import time


class MyTread(Thread):
    def __init__(self, target, args):
        # Thread.__init__(self)
        super(MyTread, self).__init__()
        self.target = target
        self.args = args
        self.rel = None

    def run(self):
        self.rel = self.target(*self.args)

    def ger_rel(self):
        return self.rel


def func(s):
    print('--开始--', s)
    time.sleep(s)
    print('--结束--', s)
    return s + 1


t1 = MyTread(target=func, args=(1,))
t2 = MyTread(target=func, args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print(t1.ger_rel())
print(t2.ger_rel())
