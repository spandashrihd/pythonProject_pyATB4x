global_b=12      #global scope

def my_function():
    a=10        #local scope, can't access outside of this function
    print(a)
    print(global_b)

def f1():
    print(global_b)

my_function()
print(global_b)
f1()