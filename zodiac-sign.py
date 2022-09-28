month = input()
date = int(input())

if month == "December" or month == "december":
    sign = "Sagittarius" if(date < 22) else "Capricorn"
elif month == "January" or month == "january":
    sign = "Capricorn" if(date < 20) else "Aquarius"
elif month == "February" or month == "february":
    sign = "Aquarius" if(date < 19) else "Pisces"
elif month == "March" or month == "march":
    sign = "Pisces" if(date < 21) else "Ares"
elif month == "April" or month == "april":
    sign = "Ares" if(date < 20) else "Taurus"
elif month == "May" or month == "may":
    sign = "Taurus" if(date < 21) else "Gemini"
elif month == "June" or month =="june":
    sign = "Gemini" if(date < 21) else "Cancer"
elif month == "July" or month == "july":
    sign = "Cancer" if(date < 23) else "Leo"
elif month == "August" or month == "august":
    sign = "Leo" if(date < 23) else "Virgo"
elif month == "September" or month == "september":
    sign = "Virgo" if(date < 23) else "Libra"
elif month == "October" or month == "october":
    sign = "Libra" if(date < 23) else "Scorpio"
else:
    sign = "Sagittarius"

print(f"Your Astrological sign is: {sign}")