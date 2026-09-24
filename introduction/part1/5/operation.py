# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation.lower() == "add":
    print(f"{number1} + {number2} = {number1+number2}")
if operation.lower() == "multiply":
    print(f"{number1} * {number2} = {number1*number2}")
if operation.lower() == "subtract":
    print(f"{number1} - {number2} = {number1-number2}")