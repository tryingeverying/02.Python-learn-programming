#! python3
# mapIt.py 根据命令行输入的参数打开其在高德地图中的检索的网址


import webbrowser, sys, pyperclip, logging

logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug('开始mapIt.py的调试')

# 从命令行中输入参数的情况
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    logging.debug(f"此时命令行输入的address值为{address}")
# 从剪切板上获取参数的情况
else:
    address = pyperclip.paste()
    logging.debug(f"此时从剪切板获取的address值为{address}")

# 使用webbrowser打开需要检索的address的web
webbrowser.open('https://ditu.amap.com/search?query=' + address)







