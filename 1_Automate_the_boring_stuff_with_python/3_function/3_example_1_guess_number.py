# 展示一个简单的猜数字游戏。在运行这个程序时，输出看起来像这样：
"""
I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!
"""
import random

def main():
    # 生成一个1到20的随机整数
    secret_number = random.randint(1,20)
    print('I am thinking of a number between 1 and 20.')

    # 六次猜数字的机会
    for i in range(7):
        # 加上对于输入结果非数字的判断
        try:
            guess_number = int(input("Take a guess."))
            if guess_number > secret_number:
                print("Your guess is too high.")
            elif guess_number < secret_number:
                print("Your guess is too low.")
            else:
                break # This condition is the correct guess!
                # 说实话 这个break我确实没想到，
                # 这种for循环特别是那种比较长的一定要预先考虑条件符号后直接终止循环的问题。
        except ValueError:
            print("请确保输入的数据为1-20间的整数")
            
    if guess_number == secret_number:
        print("Good job! You guessed my number in " + str(i) + " guesses!")
    else:
        print("Nope. The number I was thinking of was" + str(secret_number))
        # 这个超过预定次数后终止且给出随机值的我也一开始没想到

if __name__ == "__main__":
    main()
