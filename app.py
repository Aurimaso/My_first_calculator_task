import logging
from math import sqrt

logging.basicConfig(filename='calculations.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def calc_eval(x:str) -> str:
    try:
        # logging.info(f"Given match: {x} = Result: {eval(x)}")
        return str(eval(x))
    except ZeroDivisionError:
        return 'No devision from zero'
    except Exception as e:
        return 'Please try again :('

def sqrt_func(x:str) -> str:
    try:
        logging.info(f"Square root of {x}: {sqrt(float(x))}")
        return str(sqrt(float(x)))
    except ValueError:
        return ('Only numbers allowed!')
    




