#分支语句
num_1=input('输入一个数字:')
if num_1=='1':
    print('1')
else :
    print('2')
# input输入的type默认输入的是str类型

#range函数
# range函数返回一个可迭代的对象，
# 他的第三个参数是步长，
# 这样就成生成任意公差的等差数列了

#break和continue
# break的作用是提前结束循环
# continue的作用是结束本次循环，但是不打破整体的循环

#pass函数
# pass就是占位用的，替代暂时不想好的内容

#函数

def fib_recursive_1(n): #递归函数实现斐波那契数列
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive_1(n-1) + fib_recursive_1(n-2)

def fib_recursive_2(n): #循环函数实现斐波那契数列
    a,b=0,1
    #python里独有的一种语法，把=右边的值一次赋给左边
    while a < n:
        print(a,end=' ')
        # print函数里end这个参数后面的元素就是print的间隔值
        a,b = b,a+b #这个换位就很秀
        #上面这个的意思就是把a,b的值给更换掉，这个python里独特的语法还是很有意思的
    print()

print(fib_recursive_2(8))

#函数的参数问题
#python的语法是
# 函数的前面的参数有默认值了
# 则后面的参数也必须有默认值
# 即所有的没有默认值的参数写完了之后
# 才能开始写没有默认值的参数

def countdown(start=10,end=5):
    while start>end:
        start-=1
        print(start)


if __name__ == "__main__":
    countdown()
    countdown(100)
    countdown(start=5)

#任意个数的参数
#这个在参数前面加上*的意思就是可以传入任意个数的args参数
def concat(*args,sep='\t'):#\t是转义符缩进的意思
    print(type(args))
    return sep.join(args)

print(concat('abc','def','ghi'))

#lamda匿名函数
pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda p:p[1])
#sort python内置的排序函数,从小到大排序
#这个lamda函数的意思就是把排序的索引值换成了:后面的p[1]
print(pairs)

#lamda函数就是将那些简单的函数给用一句简短的lamda函数代替的方法
#用法为lamda 参数:参数执行的命令
def sum(x,y):
    return x+y
print(sum(1,2))

sum = lambda x,y : x+y
print(sum(1,2))
#就可以使用上面这个lamda表达式了代替上面那个sum函数的功能






















