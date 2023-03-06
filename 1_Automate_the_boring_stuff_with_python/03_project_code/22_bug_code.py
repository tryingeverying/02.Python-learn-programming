# import random,logging

# logging.basicConfig(level=logging.DEBUG , format='%(asctime)s- %(levelname)s - %(message)s')
# logging.debug('start of program')
# guess = ''
# guess_dict={}
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
#     if guess == 'heads':
#         guess_dict['heads'] = 1
#     elif guess == 'tails':
#         guess_dict['tails'] = 0
#     logging.debug('guess is '+ guess)
 
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# logging.debug('toss is '+ str(toss))
# logging.debug('corresponding values ' + str(guess_dict.get(guess)))
# if toss == guess_dict.get(guess):
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guesss = input()
#     logging.debug('guess is '+ guess)
#     if toss == guess:
#         print('You got it!')
#         logging.debug('corresponding values ' + str(guess_dict.get(guess)))
#     else:
#         print('Nope. You are really bad at this game.')


import random,logging
logging.basicConfig(level=logging.DEBUG , format='%(asctime)s - %(levelname)s - %(message)s')
guess = ''
logging.debug('开始程序')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('此时输入的guess为 ' + guess)
    break
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('此时生成的随机数toss为 ' + str(toss))
if toss == 0:
    toss = 'tails' 
else :
    toss = 'heads'
logging.debug('将toss转换后的值为' + toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('此时输入的guess为 ' + guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


















