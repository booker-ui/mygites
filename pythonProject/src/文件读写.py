# w 写   r 读   a 追加
fo_w = open('1.txt', mode='w', encoding='UTF-8')
fo_w.write("""你需要了解的数字证书
证书的类型：本次用到的证书类型：JKS, PKCS12。
""")
l=['苹果','香蕉']
fo_w.writelines(l)
fo_w.close()  # 关闭文件

fo_r = open('1.txt', mode='r', encoding='UTF-8')
print(fo_r.read())  # 读所有的内容
fo_r.seek(0, 0)  # 将光标移动到起始位置
print(fo_r.read())  # 读取文件10个字符
print(fo_r.readline())  # 读一行
fo_r.readlines()  # 所有内容，方法是一行为字符串的list
fo_r.close()

fo_a = open('1.txt', mode='a+', encoding='UTF-8')
fo_a.seek(0, 0)
print(fo_a.read())
fo_a.write("""
你需要了解的数字证书
证书的类型：本次用到的证书类型：JKS, PKCS12。
""")
fo_a.close()  # 关闭文件

# 图片需要以二进制形式读取
fo_img = open('../com/img.jpg', mode='rb')
print(fo_img.read())
