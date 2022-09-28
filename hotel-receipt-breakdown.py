print("Hotel Payment Breakdown: Get the breakdown of payment divided into '12% value-added tax', 'emergency fund', and 'price of accomodation'.")

amount = float(input("Input payment amount: "))

tax = amount * 0.12
amount_no_tax = amount - tax 
fund = amount_no_tax * 0.10
stay = amount_no_tax - fund

print("Tax: ", format(tax, ".2f"))
print("Emergency Fund: ", format(fund, ".2f"))
print("Accomodation: ", format(stay, ".2f"))