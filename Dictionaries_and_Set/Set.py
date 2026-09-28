
# SET:(mutable)
#set is the collection of an unordered items 
# must be set elements  immutable and unique
# not add list

collection = {1,2,3,4,5,6,4,5,"hello"}
#print(collection)
#print(type(collection))
collection.add(7)
#print(collection)
# collection.clear()  collection clear
collection.remove(3)
print(len(collection))# remove
#print(collection)

print(collection.pop()) #remove random value
#print(collection.pop())
#print(collection)

# union of set
set1={1,2,3,7}
set2={2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))