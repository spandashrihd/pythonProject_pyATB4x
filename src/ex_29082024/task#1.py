#program create a Program I will give you number(userinput and print table), f"{}" String format concept

number=float(input("enter a number for displaying table: "))
for i in range(1,11):
    print(f"{number}*{i}={number*i}")