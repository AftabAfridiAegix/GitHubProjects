# is a format used to store and exchange data.
#  It stores data in a structured format that is easy for both humans and computers to read.

# Function    	Purpose
#json.dump()  	Write Python data to a JSON file
#json.load()	Read data from a JSON file
#json.dumps()	Convert Python data into a JSON string
#json.loads()	Convert a JSON string into Python data


# Real-Life Uses of JSON
# - Medical systems: Save patient records.
# - Websites: Exchange information between frontend and backend.
# - APIs: Send and receive data between applications.
# - Settings: Store application preferences.
# - AI projects: Store configurations and structured information.

import json
student = {
    "name" : "Aftab",
    "age" : 20,
    "department" : "Computer Science"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent = 4)

print("Student data saved!")

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print("Student Name:", data["name"])

