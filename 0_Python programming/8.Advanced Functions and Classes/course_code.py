#字典类型参数
# 参数前面加入*代表输入参数是元组
# 参数前面加入**代表按照字典格式输入参数

def demo(*args_tuple, **args_dict):
  print(args_tuple)
  print(args_dict)

demo(3, 2, 1, winter=2019, has=4, came=15)
# (3, 2, 1)
# {'winter': 2019, 'has': 4, 'came': 15}

#函数调用与参数解包
def sum(a, b):
  return a + b
#最常用方式

sum(a=567, b=234)
#带上参数名，不常用

data = [123, 456]
sum(*data) # a=123, b=456
# 传入的参数去前面加*意味着对参数进行解包
# 一个*代表对序列进行解包,注意参数个待传入个数一致
data = (12, 45)
print(sum(*data)) # a=123, b=456
# 这个序列是元组也行

arg_dict = {'a':123, 'b':456}
sum(**arg_dict)
# 两个*代表对字典进行解包
# arg_dict = {'m':123, 'n':456}
# print(sum(**arg_dict))
# 传入的key必须和参数的名称一致

#函数标注
def sum(a: int, b: int) -> int:
    #参数:传入参数类型 ->输出的参数类型
  return a + b

def contact(a:str,b:str) -> str:
    return a+b

m=contact('虚竹这个挂逼','老是盗号')
print(m)

# 作用域

def scope_test():
  def do_local():
    spam = "local spam"

  def do_nonlocal():
    nonlocal spam #
    spam = "nonlocal spam"

  def do_global():
    global spam #声明下面的赋值语句作用于全局变量而不是局部变量
    spam = "global spam"

  spam = "test spam"
  do_local()
  print("After local assignment:", spam)
  do_nonlocal()
  print("After nonlocal assignment:", spam)
  do_global()
  print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

count = 1

def a():
    count = 'a函数里面'  #如果不事先声明，那么函数b中的nonlocal就会报错
    def b():
        nonlocal count #nonlocal x 如果下面给x赋予了新的值，则外层函数中的x会被变更为新赋给x的值，但是仅会改变外层函数的值，不会改变全局变量
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__': #让别人调用这个模块的时候不至于出现调试代码出现的结果
    a()
    print(count)

def demo_1(L_1):
    L_1=[1,2,3] #有赋值，此时L_1就分为了两个，一个局部一个全局
L_1=[4,5,6]
demo(L_1)
print(L_1)

def demo(L_2):
    L_2+=[1,2,3]#非赋值操作，则只是对外面那个全局变量进行更改
L_2=[4,5,6]
demo(L_2)
print(L_2)


#类
# 类的初始化方法（构造函数）
# 定义类时，可以定义一个 __init__() 函数来实现类实例化过程中的初始化工作。

class Hero:
  '''游戏中玩家操作的英雄。'''
  position = '大哥/Carry'

  def __init__(self, name):
    self.name = name

BurNing = Hero('敌法师')

# 迭代器
class Reverse:
  """Iterator for looping over a sequence backwards."""

  def __init__(self, data):
    self.data = data
    self.index = len(data)

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]

# 生成器
def reverse(data):
  for index in range(len(data) - 1, -1, -1):
    yield data[index] #yield有点像return，但是return是将整体返回，yield是返回每次迭代的结果


for char in reverse('python'):
  print(char




























































