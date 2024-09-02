#check the time taken by the test to complete

import time

def time_decorator(fun):
    def wrapper():
        start_time=time.time()
        fun()
        end_time=time.time()
        print(f"Time taken by the function is: {end_time - start_time} ")
    return wrapper()

@time_decorator
def test_ui():
    print("add a function time taken by this function")
    time.sleep(2)
