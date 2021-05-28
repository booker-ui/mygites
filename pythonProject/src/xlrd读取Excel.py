import xlrd

data = xlrd.open_workbook('test.xlsx')
sh1 = data.sheets()[0]  # 获取sheets
sh2 = data.sheet_by_name('Sheet')  # 通过名字获取sheet
sh3 = data.sheet_by_index(0)  # 通过序号获取sheet

rows_num = sh1.nrows  # 获取有多少行
cols_num = sh1.ncols  # 获取有多少列
print(rows_num)
rows = sh1.row_values(0)  # 获取第一行的值
username = sh1.col_values(0)  # 获取第一列的值
passwd = sh1.col_values(1)
value = sh1.cell_value(1, 1)
# 获取头
title = sh1.row_values(0)
# 空列表
l1 = []
# 循环取值
for i in range(1, rows_num):
    # 获取指定行的值，从第二行开始
    rows = sh1.row_values(i)
    l1.append({title[0]: rows[0], title[1]: rows[1]})
print(l1)
d1 = [{'用户名': '修改后的用户名', '密码': 'passwd1'}, {'用户名': 'user2', '密码': 'passwd2'}, {'用户名': 'user3', '密码': 'passwd3'}]
l1 = [['修改后的用户名', '密码'], ['user2', '密码'], ['user3', 'passwd3']]
