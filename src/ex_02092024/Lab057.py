class Person:
    def __init__(self, name):
        self.name=name
        print("Hello", self.name)

    def eat(self):
        print("eating")

p=Person("Bob")
print(p.name)