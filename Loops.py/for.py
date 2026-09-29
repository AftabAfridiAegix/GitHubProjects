#for loop (sequential traversal (list , string ,tuples))

nums=[1,2,3,4,5]
for val in nums:
  print(val)
 

nums=(1,2,3,4,56,7,8,9,3)
x=3
idx=0
for el in nums:
   if(el==x):
       print("number found at idx",idx)
   idx+=1


# A dictionary representing student grades
student_scores = {
    "Aftab": 95,
    "Alice": 88,
    "Bob": 72,
    "Charlie": 65
}

print("--- Student Grade Status ---")
# Using .items() to loop through keys and values simultaneously
for name, score in student_scores.items():
    if score >= 90:
        status = "Excellent"
    elif score >= 70:
        status = "Passing"
    else:
        status = "Needs Improvement"
        
    print(f"Student: {name} | Score: {score} | Status: {status}")
