a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    second = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    second = b
else:
    second = c
print("Second biggest:", second)