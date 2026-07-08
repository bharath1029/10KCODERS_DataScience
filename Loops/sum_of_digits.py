n = int(input("Enter a number : "))
sum_ = 0
while n > 0 :
  digit = n%10
  sum_ = sum_+digit
  n = n//10
print(sum_)
