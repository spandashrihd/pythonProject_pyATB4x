#Take input from the user and create a class

class Person:
    def __init__(self):
        self.name=input("enter a name: ")
        self.age = int(input("enter a age: "))
        self.phone = int(input("enter a phone number: "))
        self.occupation = input("enter occupation: ")

    def display_info(self):
        print(f"name is: {self.name}")
        print(f"age is: {self.age}")
        print(f"phone number is: {self.phone}")
        print(f"occupation is: {self.occupation}")

#Create an object
p=Person()
p.display_info()