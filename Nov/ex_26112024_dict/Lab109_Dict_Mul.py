# student_info = {
#     "name": "John",
#     "age": 25,
#     "is_on_probation": True,
#     "address": {
#         "home_address": "rampur",
#         "office_address": "kondapur"
#     }
# }
#
#
#
# student_info2 = ("name", "Jane", "age", 20, "is_on_probation", False, "address", "456 Main St")
#
# student_info3 = {
#     "name": "Johnq",
#     "age": 225,
#     "is_on_probation": True,
#     "address": {
#         "home_address": "karimnagar",
#         "office_address": "kondapura"
#     }
# }
# Student_list = [student_info, student_info2, student_info3]
# print(Student_list)
# print(Student_list[0])
# print(Student_list[0] ["name"])
# print(Student_list[0] ["age"])
# print(Student_list[0] ["address"]["home_address"] )
#
# print(Student_list[2])
# print(Student_list[2]["address"])  # Prints the home address of the third student












student_info = {
    "name": "John",
    "age": 25,
    "is_on_probation": True,
    "address": {
        "home_address": "rampur",
        "office_address": "kondapur"
    }
}

student_info2 = {
    "name": "Jane",
    "age": 20,
    "is_on_probation": False,
    "address": {
        "home_address": "456 Main St",
        "office_address": None
    }
}

student_info3 = {
    "name": "Johnq",
    "age": 225,
    "is_on_probation": True,
    "address": {
        "home_address": "karimnagar",
        "office_address": "kondapura"
    }
}

Student_list = [student_info, student_info2, student_info3]

# Print the entire list
print(Student_list)

# Access data for student 1
print(Student_list[0])  # Print all details for student 1
print(Student_list[0]["name"])  # Print name of student 1
print(Student_list[0]["age"])  # Print age of student 1
print(Student_list[0]["address"]["home_address"])  # Print home address of student 1

# Access data for student 3
print(Student_list[2])  # Print all details for student 3
print(Student_list[2]["address"])  # Print address dictionary for student 3
print(Student_list[2]["address"]["home_address"])  # Print home address of student 3
print(Student_list[2]["address"]["office_address"])  # Print office address of student 3

# Alternate way
print(student_info3["address"]["office_address"])  # Access office address of student 3 directly



# alternate way
print (student_info3 ["address"]["office_address"])



