# file: a.png
import json

# step 1: json string with some student deets
json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''

# step 2: turn that json string into a python dict
student_info = json.loads(json_string)

# step 3: print out the dict to check it out
print("python dict from json:")
print(student_info)

# file: untitled.png
import json

# step 1: make a dict with some student info
student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

# step 2: convert the dict to a json string with some pretty formatting
json_string = json.dumps(student_info, indent=4)

# step 3: print the json string to see how it looks
print("json string from dict:")
print(json_string)

# file: f.png
import json

# step 1: create a dict with student info
student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

# file where we'll save the json data
filename = 'student.json'

# step 2: write the dict to a json file
with open(filename, 'w') as file:
    json.dump(student_info, file, indent=4)
print(f"data saved to {filename}")

# step 3: read the json data back from the file
with open(filename, 'r') as file:
    data_loaded = json.load(file)

# step 4: print the loaded data to check it out
print("data loaded from json file:")
print(data_loaded)