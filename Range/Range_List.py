my_list1 = []
print("Enter objects of first list ")
for i in range(5):
    value = input("Enter your Number: ")
    n = int(value)
    my_list1.append(n)

my_list2=[]
print("Enter objects of second list: ")
for i in range(5):
    value = input("Enter your Number: ")
    n = int(value)
    my_list2.append(n)

my_list3 = my_list1 + my_list2
print(my_list3)
