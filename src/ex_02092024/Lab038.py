#decorators

def my_decorator(fun):
    def wrapper():
        print("before calling decorator")
        fun()
        print("after calling decorator")
    return wrapper()
@my_decorator
def drive_bike():
    print("I am driving")

#rive_bike()
