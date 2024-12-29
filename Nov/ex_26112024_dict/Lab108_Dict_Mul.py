student_info = {
    "name": "John",
    "age": 25,
    "is_on_probation": True,
    "address": {
        "home_address": "miyapur",
        "office_address": "kondapur"
    }
}



student_info2 = ("name", "Jane", "age", 20, "is_on_probation", False, "address", "456 Main St")

student_info3 = {
    "name": "Johnq",
    "age": 225,
    "is_on_probation": True,
    "address": {
        "home_address": "miyapura",
        "office_address": "kondapura"
    }
}
Student_list = [student_info, student_info2, student_info3]
print(Student_list)
print(Student_list[0])
print(Student_list[0] ["name"])
print(Student_list[0] ["age"])
print(Student_list[0] ["address"]["home_address"] )


print(Student_list[2]["address"]["home_address"])  # Prints the home address of the third student


# alternate way



