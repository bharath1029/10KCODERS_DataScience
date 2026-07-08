num = int(input("Enter number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

if num % sum_digits == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")