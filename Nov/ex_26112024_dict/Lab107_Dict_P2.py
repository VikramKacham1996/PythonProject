student_info = {
    "name": "John",
    "age": 25,
    "is_on_probation": True,
    "address": {
        "home_address": "miyapur",
        "office_address": "kondapur"
    }
}
print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["is_on_probation"])
print(student_info["address"])

# update student age is 100
student_info["age"] = 100
print(student_info)

student_info2 = ("name", "Jane", "age", 20, "is_on_probation", False, "address", "456 Main St")
print(student_info2)


