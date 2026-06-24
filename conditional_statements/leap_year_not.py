n = int(input("enter n :"))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) :
  print("Leap year")
else :
  print("Not a leap year")