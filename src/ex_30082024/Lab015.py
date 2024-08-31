#Grade Calculator
#write a program, that calculates ad display te letter grade for a given numerical score (eg:A,B,C,D,F based on the below grading scale)
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59


score=int(input("enter a score: "))

if 90<= score <=100:   #we can use 90<=score<=100
    print("your grade is A")
elif 80<= score <=89:
    print("your grade is B")
elif 70<= score <=79:
    print("your grade is C")
elif 60<= score <=69:
    print("your grade is D")
elif score >100:
    print("your a superman")
else:
    print("your grade is F")