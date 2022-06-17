# Decorator
from time import time
def performance(func):
    def wrapper_func(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'Time taken: {t2 - t1} s')
        return result
    return wrapper_func


@performance
def hello():
    for i in range(100000000 ):
        i * 5
    
hello()