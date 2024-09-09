#child always override the parent function
#super() -->call parent fuction

class Father:
    a=10
    def home(self):
        print("1BHK")

class Son(Father):
    b=90
    def home(self):
        super().home()              #access parent behaviour
        print(super().a)            #access parent attribute
        print("No House")
        print(self.b)

s1=Son()
s1.home()


