marks=[2, 4, 5, 7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])


student=["aftab", 20 , 55.5,"A"]
print(student[0])
student[0]="Ali"  #list mutable(change)
print(student)


marks=[34,56,45,36,33] #list slicing
print(marks[1:])

marks=[34,56,45,36,33] #list slicing
print(marks[-5:-2])

marks=[34,56,45,36,33] #list method (append in last add no.)
marks.append(3) # list mutable
print(marks) 

marks=[34,56,45,36,33] #list method (sort e.g. asc desc)
marks.sort() # list mutable
print(marks) 

# desc
marks=[34,56,45,36,33]
marks.sort(reverse=True) 
print(marks) 
#string
fruits = ["apple", "mango", "orange"]
fruits.sort()
print(fruits)

fruits = ["apple", "mango", "orange"]
fruits.sort(reverse=True)
print(fruits)

# insertion
list=[2,1,3]
list.insert(1,5)
print(list)

list=[2,1,3]
list.remove(1)
print(list)

list=[2,1,3,4,8,9,0]
list.pop(2)
print(list)

# TUPLE
#creates immutable sequence of values

marks=(1,2,3,4,5)
print(marks[0]) # index
print(type(marks))
# marks[0]=2 not allowed  immutable

# marks=(1) consider int (comma is neccessary after 1) like this (1,)

marks=(1,2,3,4,5)# slicing
print(marks[1:3])

marks=(1,2,3,4,5)
print(marks.index(5)) # find index for element

marks=(1,2,3,4,5)
print(marks.count(2))

#team = []
#team.append(input("first"))
#team.append(input("second"))
#team.append(input("third"))
#print(team)


list=[1,2,3,4,5]
copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
    print("palindrome")
else:
   print("not palindrome")