#multiple argument with no limit

def display(*args):
    print(args[0])
    print(args[1])

def display_all(*args):
    #print(args)
    for i in args:
       print(i)

display("Spanda", "Amith", "Jhon", "Bob")
display_all("Tom", 20,18, "Python", 34.9)