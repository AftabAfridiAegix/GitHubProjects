n = int(input("How many numbers you wanna enter: "))

sum = 0 

for i in range(n):
    number = int(input("Enter your number: "))
    sum = sum + number

average = sum / n

print("Sum", sum)
print("average", average)