numbers = []

n = int(input("How many you wanna enter numbers: "))
for i in range(n):
    number = int(input("Enter your number: "))
    numbers.append(number)

even_sum = 0
odd_sum = 0
for number in numbers:
    if number % 2 == 0:
        print("Even", number)
        even_sum = even_sum + number
    else:
        print("Odd", number)
        odd_sum = odd_sum + number

print("Sum of even numbers: ", even_sum)
print("Sum of odd numbers: ", odd_sum)
