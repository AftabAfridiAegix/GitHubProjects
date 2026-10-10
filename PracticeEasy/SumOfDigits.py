n = int(input("How many numbers you wanna enter: "))

total = 0
for i in range(n):
    number = int(input("Enter your number: "))
    total = total + number

print("Sum=", total)

