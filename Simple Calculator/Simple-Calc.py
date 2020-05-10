"""
Name: Simple Calculator

Purpose: A simple calculator for a number a operator and another number
"""

def maths(num1, operator, num2):
    if operator == "1":
        return num1 + num2
    elif operator == "2":
        return num1 - num2 
    elif operator == "3":
        return num1 * num2
    elif operator == "4":
        return num1 / num2
    else:
        print("invalid operator")

def main():
    num1 = int(input("Type the first number"))
    operator = input("Type the operator ( 1 to add, 2 to subtract, 3 to multiply, or 4 to divide )")
    num2 = int(input("Type the second number"))
    print(maths(num1, operator, num2))

main()