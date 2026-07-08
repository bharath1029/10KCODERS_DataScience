n = int(input("Enter n : "))
m = int(input("Enter m : "))
product = 1
for i in range (n,m+1) :
  product *= i
print(product)