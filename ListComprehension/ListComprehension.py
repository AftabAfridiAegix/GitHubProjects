# list comprehension = A concise way to create lists in python

# []
doubles=[x*2 for x in range(1,11)]
print(doubles)

grades=[85,42,34,79,78,65,30]
passing_grades=[grade for grade in grades if grade>=60]
print(passing_grades)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = [num for num in numbers if num % 2 == 0]
print(evens)  
