num = int(input("Enter number: "))

sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    