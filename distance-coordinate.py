import math

print("What is the player1's X position?")
x1 = int(input())
print("What is the player1's Y position?")
y1 = int(input())
print("What is the player2's X position?")
x2 = int(input())
print("What is the player2's Y position?")
y2 = int(input())

d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(format(d,".2f"))