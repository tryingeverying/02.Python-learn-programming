# 调试
## raise函数
- 定义自己的异常
- raise Exception('异常内容') #可以通过这种方式

```python{.line-numbers}
#实例演示
'def boxPrint(symbol,width,height)':''
'    if len(symbol) != 1':''
        raise Exception('Symbol must be a single character string.')  # 如果通过if判断则抛出自己定制的异常
'    if width <= 2':''
        raise Exception('Width must be greater than 2.')
'    if height <= 2':' '
        raise Exception('Height must be greater than 2.') 
    print(symbol * width)
'    for i in range(height - 2)':''
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
'for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3))':''
'    try':''
        boxPrint(sym, w, h) 
'    except Exception as err':' # 将前面的报错信息储存在err中以便后面的调用'
'        print('An exception happened':' ' + str(err))'

# 输出显示
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
'An exception happened':' Width must be greater than 2.'
'An exception happened':' Symbol must be a single character string.'
```

## assert函数
- 主观上判断一段代码的运行结果和自己的预想是否符合
- assert 判断条件(结果为True or False的表达式) , 条件判断是False时要显示的字符串可以通过
- 这种方式在想要的地方抛出自己想要显示的异常

```py{.line-numbers}
'market_2nd = {'ns'':' 'green', 'ew': 'red'}'
'mission_16th = {'ns'':' 'red', 'ew': 'green'}'

'def switchlights(stoplight)':' #函数实现红绿黄的三色调换'
'    for key in stoplight.keys()':''
'        if stoplight[key] == 'green'':''
            stoplight[key]='yellow'
'        elif stoplight[key] == 'yellow'':''
            stoplight[key]='red'
'        elif stoplight[key] == 'red'':''
            stoplight[key]='green'

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    # 如果判断条件是False则输出后面的内容--在实际情况中必然有一个方向的灯要是红色，故做如上断言
switchlights(mission_16th)  
switchlights(market_2nd)

#输出结果
'AssertionError':' Neither light is red! {'ns': 'green', 'ew': 'yellow'}'
```

## raise函数时针对用户可能出现的问题而出现的报错信息，assert函数是针对函数运行过程中可能出现的问题是程序自己的问题

# logging 函数
- 通过调用该函数库可以实现实时监控程序的运行情况，并且不像用print检查程序运行时要删除检查程序的print语句
```py{.line-numbers}
import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
# level 表示日志的级别，在调用高级别日志的时候低级别的日志不显示
# %(asctime)s 表示记录的时间
# %(levelname)s 表示记录的日志级别
# %(message)s 表示记录的信息

logging.debug('start of program')

'def factorial(n)':''
    logging.debug('start of factorial {0}'.format(0))
    total = 1
'    for i in range(n+1)':''
        total *=i
        logging.debug('i is '+str(i) + ', total is ' + str(total))
    logging.debug('end of factorial {0} '.format(n))
    return total

print(factorial(5))
logging.debug('end of program')

#运行结果
'2022-04-17 17':'44:07,684 - DEBUG - start of factorial 0'
'2022-04-17 17':'44:07,684 - DEBUG - i is 0, total is 0'
'2022-04-17 17':'44:07,684 - DEBUG - i is 1, total is 0'
'2022-04-17 17':'44:07,684 - DEBUG - i is 2, total is 0'
'2022-04-17 17':'44:07,685 - DEBUG - i is 3, total is 0'
'2022-04-17 17':'44:07,685 - DEBUG - i is 4, total is 0'
'2022-04-17 17':'44:07,685 - DEBUG - i is 5, total is 0'
'2022-04-17 17':'44:07,685 - DEBUG - end of factorial 5'
0
'2022-04-17 17':'44:07,686 - DEBUG - end of program'

```
### 日志级别
![日志级别](.\日志级别.jpg)

### 禁用日志
根据上面的日志级别，即在日志等级是高级别日志的时候低级别的日志不显示可以使用logging.disable(logging.CRITICAL)来禁用所有日志
```py{.line-numbers}
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s -
%(levelname)s - %(message)s')
>>> logging.critical('Critical error! Critical error!')
'2015-05-22 11':'10:48,054 - CRITICAL - Critical error! Critical error!'
>>> logging.disable(logging.CRITICAL) #在禁用最高级别的CRITICAL后，该语句后面的所有日志语句都被禁用了，如果想禁用所有日志，则可以把该语句提到import logging的后面来实现
>>> logging.critical('Critical error! Critical error!')  #日志信息就被禁用了，如果想显示日志信息就上上面那个禁用日志的语句给注释了就行了
>>> logging.error('Error! Error!')
```

### 将日志记录到文件
- 将日志信息写入到文件，让屏幕保持干净，又能保存信息

```py{.line-numbers}
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s - %(levelname)s - %(message)s') #日志信息将被记录到myProgramLog.txt文件中，而不是在终端窗口显示
```




