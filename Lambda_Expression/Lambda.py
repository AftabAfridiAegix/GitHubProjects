# Lambda Expression
# A lambda is a small, anonymous one-line function.
# Syntax: lambda arguments: expression
#
# Use:
# - For simple, quick operations
# - Commonly with map(), filter(), and sorted()
#
# Pros:
# - Short and simple
# - Useful for one-time operations
#
# Cons:
# - Hard to read if complex
# - Only one expression
#
# Rule:
# Simple/one-time task -> lambda
# Complex/reusable task -> def


square = lambda x: x ** 2
print(square(4))

add = lambda a, b: a + b
print(add(10, 20))

even = lambda x: x % 2 == 0
print(even(6))

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# CONVERT TO UPPER CASE
names = ["ali", "ahmed", "sara"]
result = list(map(lambda name: name.upper(), names))
print(result)