# Classifies a given amount of money, specified in cents as greater monetary units.

amount = float(input("Input amount here: "))

money = amount / 100
dollars = amount // 100
quarters = (amount % 100) // 25
dimes = ((amount % 100) % 25) // 10
nickels = (((amount % 100) % 25) % 10) // 5
pennies = (((amount % 100) % 25) % 10) % 5

print(money, "consists of:")
print("Dollars: ", dollars)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)