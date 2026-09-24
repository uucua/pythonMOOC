number = int(input("Please type in a number: "))

if number < 0:
    print(f"The number {number} is negative")
elif number > 0:
    print(f"The number {number} is positive")  
else:
    print(f"The number is equal to zero.")