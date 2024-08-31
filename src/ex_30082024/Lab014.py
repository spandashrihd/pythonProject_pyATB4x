#WAP to find max between 3 numbers

a=int(input("enter a first number: "))
b=int(input("enter a second number: "))
c=int(input("enter a third number: "))

if a > b and a > c:
    print(f"{a} is greater than {b} and {c}")
elif b > c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")
