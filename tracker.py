
def func_counter(func):
    def wrapper(y):
        wrapper.counter += 1
        func(y)
    wrapper.counter = 0
    return wrapper

@func_counter
def foo(y):
    return y ^ 2