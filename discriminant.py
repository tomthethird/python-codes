import math

numberA = int(input())
numberB = int(input())
numberC = int(input())

equation = (numberB**2) - (4*numberA*numberC)

if numberA == 0 and numberB == 0:
    print("There is not even an unknown in this equation!")

elif equation > 0:
    solution1 = ((-1*(numberB)) + (math.sqrt(equation))) / (2*numberA)
    solution2 = ((-1*(numberB)) - (math.sqrt(equation))) / (2*numberA)

    print(f"There are two solutions , namely {solution1} and {solution2}")

elif equation == 0:
    solution1 = ((-1*(numberB)) + (math.sqrt(equation))) / (2*numberA)
    
    print(f"There is one solution , namely {solution1}")

else:
    print("There are no solutions")