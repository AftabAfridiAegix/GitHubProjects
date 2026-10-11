n = int(input("How many numbers you wanna enter: "))

numbers = []
for i in range(n):
    number = int(input("Enter your number: "))
    numbers.append(number)

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)
        