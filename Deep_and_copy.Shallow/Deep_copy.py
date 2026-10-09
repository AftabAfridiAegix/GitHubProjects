# • Shallow Copy: Creates a new outer container, but copies the memory addresses (references) of any nested objects. If you modify a nested object in the copy, the original changes too.
# • Deep Copy: Creates a new outer container and recursively clones everything inside it onto brand-new memory addresses. The original data stays completely independent and safe.
# shallow copy When you want a new outer collection but can safely share nested data
import copy

a = [2,5,6,[5,10,20]]
b = a.copy() # b = a.deepcopy() comes an address
b[3][1] = 1000  
b[1] = 100
print(a)

# Deep copy When you need a completely independent version of complex data

a = [2,5,6,[5,10,20]]
b = copy.deepcopy(a) # b = a.deepcopy() comes an address
b[3][1] = 1000  
b[1] = 100
print(a)
