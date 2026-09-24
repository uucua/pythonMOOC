
times = int(input("How many times a wee do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groc_week = float(input("How much money do you spend on groceries in a week? "))
weekly = times * price + groc_week
print(f"Average food expenditure:")
print(f"Daily: {weekly/7} euros")
print(f"Weekly: {weekly} euros")