global_x=20

def function():
    y=40
    print(y)
    #print(global_x)  #this through error(local variable 'global_x' referenced before assignment)
    global_x=50
    print(global_x)

function()
print(global_x)
#print(y)   #through error(name 'y' is not defined), bcz can't access local variable outside the function