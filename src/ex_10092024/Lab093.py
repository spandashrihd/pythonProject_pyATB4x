#try, except, else, finally
try:
    a = int(input("enter value a: "))
    b = int(input("enter value b: "))
    c = a / b

except ValueError as ve:
    print("ValueError, you entered string, we want int")

except ZeroDivisionError as zde:
    print("Zero division error, don't use b as 0")

else:
    print(f"result is {c}")

finally:
    print("This code will be always executed")


