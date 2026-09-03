
# 1. Double a given number
double = lambda x: x * 2
print("Double:", double(10))


# 2. Find remainder
remainder = lambda x, y: x % y
print("Remainder:", remainder(10, 3))


# 3. Check whether a number is divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
print("Divisible by 5:", divisible_by_5(25))


# 4. Find smaller of two numbers
smaller = lambda x, y: x if x < y else y
print("Smaller:", smaller(10, 7))


# 5. Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
print("Fahrenheit:", celsius_to_fahrenheit(25))


# map() with lambda

# Add 5 to every number
numbers = [10, 20, 30, 40, 50]

result = list(map(lambda x: x + 5, numbers))

print("After adding 5:", result)


# Convert names to uppercase
names = ["aparna", "ravi", "priya", "kiran"]

result = list(map(lambda name: name.upper(), names))

print("Uppercase names:", result)


# filter() with lambda

# Find ages 18 and above
ages = [12, 18, 25, 15, 30, 10, 22]

result = list(filter(lambda age: age >= 18, ages))

print("Ages 18 and above:", result)


# Find names having more than 4 characters
names = ["Ram", "Aparna", "Ravi", "Priyanka", "Sai"]

result = list(filter(lambda name: len(name) > 4, names))

print("Names with more than 4 characters:", result)


# sorted() with lambda

students = [
    ("Aparna", 85),
    ("Ravi", 72),
    ("Priya", 95),
    ("Kiran", 65)
]

result = sorted(students, key=lambda student: student[1], reverse=True)

print("Students from highest to lowest marks:", result)