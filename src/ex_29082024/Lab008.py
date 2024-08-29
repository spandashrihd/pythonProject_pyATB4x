#ternary operator
age=20
print("I can go" if age>18 else "can't")

#alternative
print("I can go" if int(input("enter age: "))>18 else "Can't")

#alternative

age=int(input("enter age: "))
if age>18:
    print("I can go")
else:
    print("Can't")