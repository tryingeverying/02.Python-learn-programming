#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}


import sys, pyperclip

if len(sys.argv) < 2:
    print("请输入正确的格式：python pw.py [account] 去获取对应的密码")
    sys.exit() 
    # 因为输入的信息格式不正确一定要退出程序，要不后的程序会继续执行引发错误

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("密码已经粘贴到了粘贴板上")
else:
    print("密码箱中没有对应的账号信息")

