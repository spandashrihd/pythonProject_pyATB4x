#✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24


number=int(input("enter a number: "))

fact=1

for x in range(1, number+1):
    fact=fact*x

print(f"factorial of a number {number} is : {fact}")