
def func_counter(func, y):
    def wrapper():
        wrapper.counter += 1
        func(y)
    wrapper.counter = 0
    return wrapper

@func_counter
def foo(y):
    return y ^ 2
