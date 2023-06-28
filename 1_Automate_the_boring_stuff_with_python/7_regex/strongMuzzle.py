#! python3
# 检测强密码
"""
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
强口令的定义是：长度不少于8个字符，同时包含大写和小写字符，
至少有一位数字。你可能需要用多个正则表达式来测试该字符串，
以保证它的强度。
"""
import re 

def strongPassword(text):
    regexList = [r"[a-zA-Z0-9]{8,}",r"[a-z]+",r"[A-Z]+",r"[0-9]+"]
    for i in regexList:
        pwdRegex = re.compile(i).search(text)
        if pwdRegex is None:
            print("密码需要保证同时长度兼顾大于八位，小写字母，大写字母和数字至少一位")
            return
            # 在绝大多数情况下，当函数体内的程序执行到return这一步时，
            # 会退出函数，即使是在一个循环体内，程序也不会再执行
    print("密码匹配正确")
    # re.compile(r"[a-z]+",r"[A-Z]+",r"[0-9]+")
    # 上述正则表达式匹配的结果是前几位为至少一位的小写字母
    # 之后是至少一位的大写字母最后是至少一位的数字，
    # 顺序必须对上 要不就没有匹配项
    # AwadAS123 能够匹配 结果是wadAS123
    # 123ASDaskdbn 就无法匹配
  

password = input("请输入待检测的密码")
strongPassword(password)












