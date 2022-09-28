import math

l = int(input())
x = int(input())

area = (x * l * l) / (4 * (math.tan(math.pi / x)))

print(format(area,".2f"))