import time

def doubler(func):
    def wrapper():
        time_rn = time.time()
        func()
        time_done = time.time()
        print("Time Taken: " + str(time_done - time_rn))
        
        time_rn = time.time()
        func()
        time_done = time.time()
        print("Time Taken: " + str(time_done - time_rn))
    return wrapper

# random function to test its time
@doubler
def func():
    x = 0
    while x < 1000000:
        x += 1
        
func()