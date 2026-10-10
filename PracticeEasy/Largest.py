n = int(input("How many numbers you wanna enter: "))

numbers=[]

for i in range(n):
    number = int(input("Enter you number: "))
    numbers.append(number)

largest = numbers[0]

for number in numbers:
   if number > largest:
    largest = number

second = numbers[0]
for number in numbers:
   if number > second and number < largest:
      second = number


print("Largest", largest)
print("Second Largest", second)