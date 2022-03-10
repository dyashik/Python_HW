import time

def calculate_time(func):
    
    def wrapper():
        time_rn = time.time()
        func()
        time_done = time.time()
        print("Total time " + str(time_done - time_rn))
        
    return wrapper

# random function to test its time
@calculate_time
def func():
    x = 0
    while x < 1000000:
        x += 1