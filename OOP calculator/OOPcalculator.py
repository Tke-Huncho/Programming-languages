# MATERE HANS WALUBENGO
# SCT 211-0080/2022

class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error, division by 0"
        else:
            return num1 / num2


computeNumber = Calculator()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator(+, -, *, /): ")

if operator == "+":
    result = computeNumber.addition(num1, num2)
elif operator == "-":
    result = computeNumber.subtraction(num1, num2)
elif operator == "*":
    result = computeNumber.multiplication(num1, num2)
elif operator == "/":
    result = computeNumber.division(num1, num2)
else:
    result = "Invalid operator"

print(f"Result: {result}")
