#Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1==num2:
    print(f"both {num1} and {num2} are equal")
else:
    print(f"{num1} is lesser than {num2}")