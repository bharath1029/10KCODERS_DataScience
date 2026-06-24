a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))

if a >= b and a >= c:
    print("Biggest is ",a)
elif a <= b and b >= c:
    print("Biggest is ",b)
else:
    print("Biggest is " ,c)