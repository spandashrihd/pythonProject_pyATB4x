'''
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
'''

num1=int(input("enter a first number: "))
num2=int(input("enter a second number: "))

print(f"Maximum of number {num1} and {num2} is : ", max(num1,num2))
print(f"Power of number {num1} to {num2} is : ", pow(num1,num2))
print(f"Addition of number {num1} and {num2} is : ", num1+num2)
print(f"Product of number {num1} and {num2} is : ", num1*num2)
print(f"Subtraction of number {num1} and {num2} is : ", num1-num2)
print(f"Division of number {num1} and {num2} is : ", num1/num2)

