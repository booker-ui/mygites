import pymysql

# 创建数据库连接
conn = pymysql.connect(host='10.168.8.10',
                       user='gaoji',
                       password='123456',
                       database='test',
                       port=3306)
# 创建游标
cursor = conn.cursor()
cursor.execute('insert into student values("hei",29,"女")')
cursor.execute('update student set name="gui" where name="li"')
cursor.execute('delete from student where name="chen"')
conn.commit()
conn.close()