# Perform basic calculations on user inputted numbers

from ast import operator


num1 = float(input("\nEnter the first number: "))
operator = input("\nOperator: ")
num2 = float(input("\nEnter the second number: "))

if operator == "+":
    print("\nAddition: ", num1 + num2)
elif operator == "-":
    print("\nSubtraction: ", num1 - num2)
elif operator == "*":
    print("\nMultiplication: ", num1 * num2)
elif operator == "/":
    print("\nDivision: ", num1 / num2)
else:
    print("\nThis is not a valid operator")
