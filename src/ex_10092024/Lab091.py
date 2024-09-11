# a=int(input("enter value a: "))
# b=int(input("enter value b: "))
# c=a/b
#
# print("result is: ", c)

#fixing above exceptions
try:
    a = int(input("enter value a: "))
    b = int(input("enter value b: "))
    c = a / b
    print("result is: ", c)

except Exception as e:
    print(e)
    print("please check your input, it should not be zero or string")

