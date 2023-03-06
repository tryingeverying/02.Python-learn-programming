#10——1
def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')  #自己编辑的报错，即在符合条件时抛出这个错误信息
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h) 
    except Exception as err: #将错误信息储存在err中以便后面的调用
        print('An exception happened: '+ str(err))

# 10——2

import traceback

try:
    raise Exception('this is the error maeesge.')
except:
    errorfile=open('errorinfo.txt','w')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('the traceback info was written to errorinfo.txt')

# 10——3
market_2nd = {'ns':'green', 'ew': 'red'}
mission_16th = {'ns':'red', 'ew': 'green'}

def switchlights(stoplight) : #函数实现红绿黄的三色调换
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key]='yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key]='red'
        elif stoplight[key] == 'red':
            stoplight[key]='green'

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    # 在实际情况中必然有一个方向的灯要是红色，故做如上断言
switchlights(mission_16th)  
switchlights(market_2nd)

#10——4

import logging
logging.basicConfig(filename='日志文件.txt', level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('start of program')

def factorial(n):
    logging.debug('start of factorial {0}'.format(0))
    total = 1
    for i in range(n+1):
        total *=i
        logging.debug('i is '+str(i) + ', total is ' + str(total))
    logging.debug('end of factorial {0} ' .format(n))
    return total

print(factorial(5))
logging.debug('end of program')

#10——5
import random

heads = 0
for i in range(1,1001):
    if random.randint(0,1):
        heads=heads+1
    if i == 500:
        print('halfway done !')

print('heads came up ' + str(heads) + 'times .')










