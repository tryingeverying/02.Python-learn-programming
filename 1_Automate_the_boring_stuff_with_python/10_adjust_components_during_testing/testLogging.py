import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of program")

def factorial(n):
    # logging.debug(f'start of factorial{(%s%%)}'%(n))
    logging.debug(f'start of factorial {(n)}')
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('end of factorial (%s)'%(n))
    return total

# logging.disable(logging.CRITICAL)
print(factorial(6))