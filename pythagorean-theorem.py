import math

a = int(input("Input value of 'a': "))
b = int(input("Input value of 'b': "))
c = math.sqrt((a ** 2) + (b ** 2))

output = "The length of the diagonal is {:.3f}."

print(output.format(c))