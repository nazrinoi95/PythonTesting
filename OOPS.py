# classes for calculator functions to demo object oriented programming
# Classes will have variables / methods
# Self is needed to call variables inside methods (instance variables)

class Calculator:
    num = 100 #class variables will remain constant
    # Default constructor will be called everytime class is called
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print ("I am called as a constructor")
    def getData(self):
        print ("now executing as method in class")
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

if __name__ == "__main__": # this function is to protect other imports from running the main parent object in their resp file
    obj = Calculator(2, 3)  # syntax to create objects in python , instance variable is inserted here
    obj.getData()
    print(obj.Summation())

    obj1 = Calculator(3, 5)  # syntax to create objects in python , instance variables
    obj1.getData()
    print(obj1.Summation())

