"""
编写一个名为collatz()的函数，它有一个名为number的参数。
如果参数是偶数，那么collatz()就打印出number // 2，并返回该值。
如果number是奇数，collatz()就打印并返回3 * number + 1。
"""

def collatz(number):
    if number % 2 == 0:
        r_number = number // 2
    else:
        r_number = 3 * number + 1
    return r_number

def main():
    try:
        number = int(input("请输入一个整数\n3"))
        while number != 1:
            number = collatz(number)
            print(number)

    except ValueError:
        print("请保证输入值为整数")

if __name__ == "__main__":
    main()











