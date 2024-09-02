class Person:
    def __init__(self):
        print("I will be automatically called when object is created")


    def walk(self):
        print("I am walking")

#creating a object
p=Person()
p.walk()
