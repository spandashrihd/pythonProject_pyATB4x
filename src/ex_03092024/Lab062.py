#Login page authetication

class VWOLogin:
    def __init__(self, email, password):
        self.email=email
        self.password=password

    def login_confirm(self):
        if self.email=="spanda@gmail.com" and self.password=="Pass123":
            print("Allowed to login")
        else:
            print("Not allowed to login")

email=input("enter email address: \n")
password=input("enter password: \n")

login=VWOLogin(email, password)
login.login_confirm()