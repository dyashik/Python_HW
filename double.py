import time

def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper

# random function to test its time
@doubler
def func():
    x = 0
    while x < 1000000:
        x += 1
