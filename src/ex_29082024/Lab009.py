#Write a program to calculate the area of the circle using formula area=pi*r^2, take radius as user input
import math
pi=3.14
r=float(input("enter the radius: "))
area=pi*math.pow(r,2)
print(f"area of the circle is: {area}")