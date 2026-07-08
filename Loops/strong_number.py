num = int(input("Enter number: "))

temp = num
sum_factorial = 0

while temp > 0:
    digit = temp % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_factorial += factorial
    temp //= 10

if sum_factorial == num:
    print("Strong Number")
else:
    print("Not a Strong Number")