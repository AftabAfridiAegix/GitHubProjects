n = int(input("How many numbers you wanna enter: "))
numbers = []
for i in range(n):
    number = int(input("Enter your number: "))
    numbers.append(number)
target = int(input("Enter your target: "))

count = 0

for number in numbers:
    if number == target:
     count += 1

print("count", count)
