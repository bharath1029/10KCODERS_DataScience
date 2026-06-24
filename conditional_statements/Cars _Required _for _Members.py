import math

members = int(input("Enter number of members: "))

cars_needed = math.ceil(members / 5)

print("Cars needed =", cars_needed)