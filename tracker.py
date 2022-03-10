
def func_counter(y):
    def decorator(func):
        def wrapper(*args, **kwargs):
            wrapper.counter += 1
            func(y)
        wrapper.counter = 0
        return wrapper
    return decorator