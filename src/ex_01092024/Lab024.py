#match statement, it behaves like a switch statement in C
#WAP to ask user, which browser he wants to run automation

browser_name=input("enter the name of browser: ")
browser_name=browser_name.lower()      #user might enter capital
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _:   #like default
        print("Browser Not Found")


