info={
    "name": "comsats",
    "subjects" : ["python", "c", "Java"],# list
    "topics" : ("dict", "set"), # tupple
    "age":35,
    "is_adult" : True,
    12.99 : 94.4
}
# null_dict ={}  # null dictionary
# print(null_dict)


# info["name"] = "Ali"
# info["surname"] = "Khan"
# print(info)




student = {
"name" : "aftab afridi",
   "subjects" :{
       "phy" : 97,
       "chem" : 98,
       "urdu": 56,
       
   }

}
#print(student)
#print(student["subjects"])
#print(student["subjects"]["chem"])
#print(student.keys())
#print(list(student.keys()))
#print(len(student.keys()))
print(list(student.items()))#pairs
print(student.get("name2")) #no error
student.update({"city" : "peshawar"})
print(student)