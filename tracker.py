
counter = 0

def func_counter(func):
    
    def wrapper(y):
        wrapper.counter += 1
        func(y)
        
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y^2

foo(3)
foo(3)
print(foo.counter) # expect 2 as output