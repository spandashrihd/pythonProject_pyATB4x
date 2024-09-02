#OOP
class Dog:
    #Attriute
    Name=None
    Breed=None
    Color=None

    #behavior
    def sleep(self):
        print("sleeping")

    def bark(self):
        print("Bark")
 
#creating an object
dog=Dog()
print(dog.Name)
dog.Name="Tom"
print(dog.Name)
dog.sleep()
dog.bark()