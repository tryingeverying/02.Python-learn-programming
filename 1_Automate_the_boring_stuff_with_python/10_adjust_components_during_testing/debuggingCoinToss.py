#! python3

import random, logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("开始程序")

guess = ''
while guess not in ('heads', 'tails'):

    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f"此时的guess值为{guess}")

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 1:
    toss = "heads"
elif  toss == 0:
    toss = "tails"
logging.debug(f"此时的猜测值guess为{guess}，随机值toss为{toss}")

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')









