import pymysql

# 创建数据库连接
conn = pymysql.connect(host='10.168.8.10',
                       user='gaoji',
                       password='123456',
                       database='test',
                       port=3306)
# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select * from student')
# print(cursor.rowcount)  # 记录的数据
# # print(cursor.fetchone())  # 获取一条
# # print(cursor.fetchone())  # 获取下一条
# # print(cursor.fetchall())  # 所有剩下的记录
# print(cursor.fetchmany(2))  # 获取指定条数记录
rows = cursor.fetchall()
cursor.close()
for row in rows:
    print(row)
conn.close()