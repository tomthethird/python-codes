intensity = float(input())

if intensity >= 10:
    print("Meteoric")
elif intensity >= 8 and intensity < 10:
    print("Great")
elif intensity >= 7 and intensity < 8:
    print("Major")
elif intensity >= 6 and intensity < 7:
    print("Strong")
elif intensity >= 5 and intensity < 6:
    print("Moderate")
elif intensity >= 4 and intensity < 5:
    print("Light")
elif intensity >= 3 and intensity < 4:
    print("Minor")
elif intensity >= 2 and intensity < 3:
    print("Very minor")
else:
    print("Micro")