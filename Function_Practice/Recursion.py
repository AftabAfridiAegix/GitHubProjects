# Recursion 
# def  : when a function call itself repeatedly

# if (n==o) : Base Case

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
#show(5)


# FACTORIAL

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)

#print(fact(5))

# calculate sum of first n natural numbers.
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum=calc_sum(5)
#print(sum)

# write a recursive function to print all elements in a list

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])

    print_list(list, idx+1)
fruits =["mango", "litchi", "apple", "banana"]
print_list(fruits)

