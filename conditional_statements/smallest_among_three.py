a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))

if a <= b and a <= c:
    print("smallest is ",a)
elif a >= b and b <= c:
    print("smallest is ",b)
else:
    print("smallest is ",c)