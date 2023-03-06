def collatz(number):
    if number % 2 == 0:# %是求余运算 //是除二取整运算
        num_c=number//2
        print(num_c)
    else:
        num_c=3*number+1
        print(num_c)
        
    return num_c

try :
    num_1=int(input('请输入一个整数'))
    while True:
        num_1 = collatz(num_1)
        if num_1 == 1:
            break
except ValueError:
    print('请确保输入的一个整数')
