# Jonathan Davila, 07/15/2025, M8.2 Assignment: JSON Practice
# This program reads the JSON file to print the orginal student list, appends a new user then checks and updates the list. 

import json


# Created a function that loops through the list and prints students details in a formatted line.
def list_students(student_info):
    for j in student_info:
        print(f"{j[ 'L_Name']}, {j['F_Name']}, : ID = {j['Student_ID']}, Email = {j['Email']}")
# Created a function that checks if the new student already exists in the list 
def check_student(student_list, new_student):
    if new_student not in student_list:
        student_list.append(new_student)
    #Read the student JSON file    
with open("student.json", "r") as j:
    student = json.load(j)

print("*This is the original student list*")
list_students(student)
# Add a new entry.
new_student = {
    "F_Name": "Jonathan",
    "L_Name": "Davila",
    "Student_ID": 106321,
    "Email": "j.davila@gmail.com"
}
# Add the new student if they are not already in the list.
check_student(student, new_student)

print("\n *This is the updated student list*")
list_students(student)
# Writes and saves the updatd student list to the Student1 JSON file
with open("student.json", "w") as j:
    json.dump(student, j, indent=2)