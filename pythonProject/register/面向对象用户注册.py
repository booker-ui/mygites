'''
1、实现注册功能
输入：username、password，cpassword
#3个都不能为空
#用户名长度最少6位， 最长20位，用户名不能重复
#密码长度最少8位，最长15位
#两次输入的密码要一致
#注册成功之后，要写到文件(txt文件)里面
'''


class Register():
    # 用初始化户名和密码
    def __init__(self, username, password, cpassword):
        self.username = username
        self.password = password
        self.cpassword = cpassword
        self.msg = ''
        self.main()

    # 判断用户名长度是否合法
    def __userNameLen(self):
        if len(self.username) == 0:
            self.msg = '用户名不能为空'
            return False
        elif len(self.username) < 6 or len(self.username) > 20:
            self.msg = '用户名长度最少6位， 最长20位'
            return False
        else:
            return True

    # 判断用户名是否唯一
    def __userNameUnique(self):
        """
        判断用户是否唯一
        """
        try:
            with open('users.txt', 'r', encoding='UTF-8') as f:
                for userName in f.readlines():
                    if userName.strip().split(',')[0] == self.username:
                        self.msg = '此用户已经被注册！'
                        return False
                return True
        except FileNotFoundError:
            # 创建一个文件
            with open('users.txt', 'w', encoding='utf-8') as f:
                f.write('用户名，密码\n')
                return True

    # 判断密码长度是否合法
    def __passwdLen(self):
        if len(self.password) == 0:
            self.msg = '密码不能为空'
            return False
        elif len(self.password) < 8 or len(self.password) > 15:
            self.msg = '密码长度最少8位，最长15位'
            return False
        else:
            return True

    # 判断确认密码和密码是否一致
    def __diffPasswd(self):
        if self.password.strip() != self.cpassword.strip():
            self.msg = '密码和确认密码不一致！'
            return False
        else:
            return True

    # 注册用户，将用户信息保存到文件当中
    def __regUser(self):
        try:
            with open('users.txt', 'a') as f:
                f.write(self.username + "," + self.password + '\n')
            self.msg = '恭喜你，注册成功！'
            return True
        except Exception as msg:
            self.msg = msg
            return False

    def main(self):
        while True:
            # 对用户名进行判断
            res1 = self.__userNameLen()
            if not self.__userNameLen():  # 用户名长度是否合法
                print(self.msg)
                break

            if not self.__userNameUnique():  # 用户名是否唯一
                print(self.msg)
                break
            # 对密码进行判断
            if not self.__diffPasswd():  # 密码长度和鱼确认密码是否一致
                print(self.msg)
                break
            if not self.__passwdLen():  # 密码从长度
                print(self.msg)
                break

            self.__regUser()
            break


stu = Register('11111111', '11111111', '11111111')
