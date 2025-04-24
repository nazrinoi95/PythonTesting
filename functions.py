# Declaring the functions
def salutations(name):
    print ("Hello " + name)

def tambah (a,b):
    print (a + b )

def GreetUser(username):
    print(f"Hello, {username}! Welcome to the Python course.")

# Calling the functions

salutations("Nazrin")# 1st function

tambah(2,.3)# 2nd function

GreetUser("John")# 3rd function


def CalculateAverage(*args):
    numbers=[args]
    average=sum(args)/len(args)
    print(f"The average of {args} are {average}")

CalculateAverage(1,10,23,222)