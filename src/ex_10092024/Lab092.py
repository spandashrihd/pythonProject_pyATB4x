import math
#math.exp(1000)        OverflowError: math range error

try:
    print(math.exp(1000))
    #print(math.exp(4))
except Exception as e:
    print(e)
    print("please try to use lower exponent value")

