'''
Create a Employee Class
A - name,age, phone, address, eid
B - walk, talk, print details,
with the Constructor which will set the values
Ask the user about the information for E1, E2
print the details of the E1, E2 via the print employee functions.
'''

class Employee:

    #constructor to set the attributes
    def __init__(self, name, age, phone, address, eid):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.eid=eid

    #Behavior
    def walk(self):
        print(f"{self.name} walk slowly")

    def talk(self):
        print(f"{self.name} talk loudly")

    #Behavior to display the employee daat
    def employee_data(self):
        print(f"Below are the Employee {self.name} data : ")
        print(f"Name: {self.name}\n Age: {self.age}\n Phone: {self.phone}\n Address: {self.address}\n Employee_ID: {self.eid}")

#asking user input for Employee_1 information
print("Please enter Employee_1 info")
name1=input("enter the name of the employee: ")
age1=int(input("enter the age of the employee: "))
phone1=int(input("enter the phone number of the employee: "))
address1=input("enter teh address of the employee: ")
eid1=int(input("enter the Employee id: "))

#asking user input for Employee_2 information
print("Please enter Employee_2 info")
name2=input("enter the name of the employee: ")
age2=int(input("enter the age of the employee: "))
phone2=int(input("enter the phone number of the employee: "))
address2=input("enter teh address of the employee: ")
eid2=int(input("enter the Employee id: "))


#Creating object E1 & E2, with argument
E1=Employee(name1,age1,phone1,address1,eid1)
E2=Employee(name2,age2,phone2,address2,eid2)

#Calling E1 methods
E1.walk()
E1.talk()
E1.employee_data()

#Calling E2 methods
E2.walk()
E2.talk()
E2.employee_data()

