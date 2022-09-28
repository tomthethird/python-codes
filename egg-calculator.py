# 12 eggs for the price of 10! Buyers are encouraged to buy whole trays of eggs for the savings.
# Eggs that don’t make a dozen are sold at the individual price of Php 7.

print("Egg Calculator: Buy 1 for Php 7. Buy a dozen for Php 70.")

egg_quantity = int(input("How many pieces of egg? Type here:"))
dozen = egg_quantity // 12
single_egg = egg_quantity % 12
totalPrice = (dozen * 70) + (single_egg * 7)

print(totalPrice)