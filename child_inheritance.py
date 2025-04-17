# can call methods from other file through object
from OOPS import Calculator # import from this specific file filename / class

class childImplement(Calculator): #insert class here to include the other files class
    num2= 200

    def __init__(self):# Child constructor should also call the parent constructor
        Calculator.__init__(self,2,3)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

CH1 = childImplement()
CH1.getCompleteData()
print (CH1.getCompleteData())