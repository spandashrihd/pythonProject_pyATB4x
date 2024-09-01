#✅ Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13


n=int(input("enter a number to print fibonacci series: "))

n1,n2=0,1
fib_series=[0,1]

for x in range(1,n+1):
    nth=n1+n2
    fib_series.append(nth)
    n1 = n2
    n2 = nth

print(f"fibonacci series for the given range is: {fib_series}")

