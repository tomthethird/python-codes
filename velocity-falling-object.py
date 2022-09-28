# Calculate velocity of a falling object with Earth's constant gravity 9.8 m/s^2 and initial velocity of 0m/s. Where 'd' is distance, 'vi' is initial velocity.
from math import sqrt

d = int(input("Input distance here: "))
vi = 0
velocity = sqrt((vi ** 2) + 2 * 9.8 * d)

print(format(velocity, ".2f"))