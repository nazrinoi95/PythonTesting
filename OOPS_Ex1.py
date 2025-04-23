class BasicCalculator:

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        if self.secondNumber == 0:
            return "Error: secondNumber cannot be 0" #To handle if input equates to 0
        return self.firstNumber / self.secondNumber


result = BasicCalculator(10, 0)
print(f"Addition: {result.firstNumber} + {result.secondNumber} = {result.addition()}")
print(f"Subtraction: {result.firstNumber} - {result.secondNumber} = {result.subtraction()}")
print(f"Multiplication: {result.firstNumber} * {result.secondNumber} = {result.multiplication()}")
print(f"Division: {result.firstNumber} / {result.secondNumber} = {result.division()}")
