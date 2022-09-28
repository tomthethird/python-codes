print("Compound Interest Calculator: Calculate how much money earn after some time with a fixed interest rate.")

principal = float(input("Input initial deposit: "))
rate = int(input("Input interest rate: "))
years = int(input("Input how many years: "))

rate = rate/100
savings = principal * ((1 + rate) ** years)

print(format(savings, ".2f"))