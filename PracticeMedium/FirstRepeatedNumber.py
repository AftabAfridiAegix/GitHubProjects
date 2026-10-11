n = int(input("How many numbers you wanna enter: "))
numbers = [] 
for i in range(n):
    number = int(input("Enter your number: "))
    numbers.append(number)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            print("First Repeated number", numbers[i])
            break
    else:
        continue
    break
