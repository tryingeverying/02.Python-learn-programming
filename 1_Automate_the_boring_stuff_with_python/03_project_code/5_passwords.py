#! python3   
# pw.py - An insecure password locker program.
#如果你想从命令行运行命令就必须有#！ python3
PASSWORDS = {'email': '1234abd',
'blog': 'abcdefg',
'luggage': '12345'}
import sys
import pyperclip
if len(sys.argv) < 2: #sys.argv 获取在命令行输入的命令，并储存为list
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 
#sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始
# first command line arg is the account name
print (account)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
 
#测试命令：打开CMD，输入py.exe + 文件名（绝对路径）+ 命令内容，
#比如：py.exe D:\python_work\口令保管箱.py email
