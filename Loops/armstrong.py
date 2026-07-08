n = int(input("Enter a number : "))
original=n
sum_of_cubes = 0
while n > 0 :
  digit = n%10
  sum_of_cubes = sum_of_cubes+(digit**3)
  n = n//10
if sum_of_cubes == original :
  print("Armstrong number")
else :
  print("Not armstrong number")
