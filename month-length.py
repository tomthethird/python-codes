month = int(input())
if month == 2:
    print("28 or 29 days")
elif (month % 2) == 0 and month >= 8:
    print("31 days")
elif (month % 2) == 1 and month >= 8:
    print("30 days")
elif(month % 2) == 0:
    print("30 days")
else:
    print("31 days")