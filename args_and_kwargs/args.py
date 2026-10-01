# *args
# Collects values in a tuple

def add(*args):
    print(args)
add(10, 20, 30, 40)

def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)
add(10, 20, 30)
 # find maximum

def maximum(*args):
    return max(args)
print(maximum(12, 45, 7, 89, 23))

def duplicates(*args):
    for num in args:
        if args.count(num) > 1:
            print(num)
duplicates(2, 3, 3, 4, 5, 6,  8)