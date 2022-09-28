from math import radians, sin, cos

velocity = int(input())
angle = int(input())
time = float(input())

angle = radians(angle)

x = round(velocity * cos(angle) * time)
y = round((velocity * sin(angle) * time) - (0.5 * 9.81 * time ** 2))

print(f"{x}, {y}")