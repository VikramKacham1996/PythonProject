my_dict = {
    'name': 'Vikky',
    'age': 20,
    'city': 'New York',
    'role': 'functional tester',
    'is_active': True,
    'skills': ['Python', 'Java', 'C++'],
    'hobbies': ['reading', 'writing', 'coding'],
    'education': 'Bachelor of Science in Computer Science',

    'experience': '6.6 years'
}

print(my_dict)
print(my_dict['name'])

print(my_dict['age'])
print(my_dict['skills'])
print(my_dict['hobbies'])
print(my_dict['education'])
print(my_dict['experience'])
del my_dict['experience']  # Deleting the key 'experience' from the dictionary
my_dict ["age"]= "30" # updating
my_dict["friend"] = "Vikky" # adding
dict() # empty dict also

print(my_dict)

for key, value in my_dict.items(): # iterating
    print(f"{key}: {value}")

    # Checking if 'age' exists in the dictionary
print("age" in my_dict)
print("name" in my_dict)
print("experience" in my_dict)









#  Chat gpt Method	Description
# dict.clear()	Removes all elements from the dictionary.
# dict.copy()	Returns a shallow copy of the dictionary.
# dict.get(key[, default])	Returns the value for the specified key if it exists; otherwise, returns the default value.
# dict.items()	Returns a view object with key-value pairs ((key, value)).
# dict.keys()	Returns a view object with all keys in the dictionary.
# dict.values()	Returns a view object with all values in the dictionary.
# dict.pop(key[, default])	Removes the key and returns its value. If key is not found, returns the default value if provided.
# dict.popitem()	Removes and returns the last inserted (key, value) pair as a tuple.
# dict.setdefault(key[, default])	Returns the value for the key if it exists; otherwise, inserts the key with a default value.
# dict.update([other])	Updates the dictionary with elements from another dictionary or iterable of key-value pairs.
# dict.fromkeys(seq[, value])	Creates a new dictionary with keys from the sequence and sets them to the specified value.