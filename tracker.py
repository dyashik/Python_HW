
def func_counter(func):
    def wrapper():
        wrapper.counter += 1
        func()
    wrapper.counter = 0
    return wrapper