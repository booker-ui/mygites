import time, datetime

print(time.time())  # 当前系统的时间，
print(time.localtime())  # 当前时间对象
print(time.localtime().tm_wday)  # 今天是星期几（从0开始）
print(time.localtime().tm_mday)  # 今天是几号
now = time.ctime()
str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
strtime = time.strftime('%m%d%H%M%S', time.localtime())
print(strtime)
time.sleep(3) # 固定等待时间
print(str(time.time())[:10])
