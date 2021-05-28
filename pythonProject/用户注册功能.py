'''
1、实现注册功能
输入：username、password，cpassword
#最多可以输错3次
#3个都不能为空
#用户名长度最少6位， 最长20位，用户名不能重复
#密码长度最少8位，最长15位
#两次输入的密码要一致
#注册成功之后，要写到文件(txt文件)里面
'''

class Register():
    #用初始化户名和密码
    # def __init__(self,username,password,cpassword):
    #     self.username = username
    #     self.password = password
    #     self.cpassword = cpassword

    #判断用户名长度是否合法
    def userNameLen(self,username):
        if len(username) == 0:
            return '用户名不能为空'
        elif len(username) < 6 or len(username) > 20:
            return '用户名长度最少6位， 最长20位'
        else:
            return True
    #判断用户名是否唯一
    def userNameUnique(self,username):
        # print('判断用户是否唯一')
        try:
            with open('users.txt','r') as f:
                for userName in f.readlines():
                    # print(userName.strip())
                    if userName.strip().split(',')[0] == username:
                        # print(userName.strip())
                        return '此用户已经被注册！'
                return True
        except FileNotFoundError:
            #创建一个文件
            with open('users.txt','w',encoding='utf-8') as f:
                f.write('用户名，密码\n')
                return True
    #判断密码长度是否合法
    def passwdLen(self,password):
        if len(password) == 0:
            return '密码不能为空'
        elif len(password) < 8 or len(password) > 15:
            return '密码长度最少8位，最长15位'
        else:
            return True
    #判断确认密码和密码是否一致
    def diffPasswd(self,password,cpassword):
        if password.strip() != cpassword.strip():
            return '密码和确认密码不一致！'
        else:
            return True

    #注册用户，将用户信息保存到文件当中
    def regUser(self,username,passwd):
        try:
            with open('users.txt','a') as f:
                f.write(username+","+passwd +'\n')
            return '恭喜你，注册成功！'
        except Exception as msg:
            return msg

    #提示用户剩余的注册次数
    def promptTimes(self,times):
        if times != 0:
            return "你还有"+str(times)+"次机会！请重新输入信息。"
        else:
            return "注册失败次数过多，请稍后再注册！"

if __name__ == "__main__":
    #注册主程序
    times = 3
    user = Register()
    #对用户名进行判断
    while times >= 1:
        userName = input('用户名：')
        res1 = user.userNameLen(userName)
        if res1 != True:
            print(res1)
            times -= 1
            print(user.promptTimes(times))
            continue
        res2 = user.userNameUnique(userName)
        if res2 != True:
            print(res2)
            times -= 1
            print(user.promptTimes(times))
            continue
        #对密码进行判断
        while times >= 1:
            passwd = input('密码：')
            res3 = user.passwdLen(passwd)
            if res3 != True:
                print(res3)
                times -= 1
                print(user.promptTimes(times))
                continue
            #对确认密码进行判断
            while times >= 1:
                cpasswd = input('确认密码：')
                res4 = user.diffPasswd(passwd,cpasswd)
                if res4 != True:
                    print(res4)
                    times -= 1
                    print(user.promptTimes(times))
                else:
                    times -= 1
                    break
            break
        #注册用户
        if res1 == True and res2 == True and res3 == True and res4 == True:
            res5 = user.regUser(userName,passwd)
            print(res5)
        break
