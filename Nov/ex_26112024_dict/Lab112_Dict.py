dict1={"a":1, "b":2, "c":3}
dict2={"a":1,"b":2}

missing_keys = set(dict1.keys())-set(dict2.keys())
print(missing_keys)


missing_values = set(dict1.values())-set(dict2.values())
print(missing_values)

# Sort a dictionary by it's  values in descending order

my_dict1={"a":3, "b":1, "c":2}



###################

my_dict1 = {"a": 3, "b": 1, "c": 2}

# Sort the dictionary by values in descending order
sorted_dict = dict(sorted(my_dict1.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict)
###################

my_dict1 = {"a": 3, "b": 1, "c": 2}

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(my_dict1.items(), key=lambda item: item[1]))

print(sorted_dict)

