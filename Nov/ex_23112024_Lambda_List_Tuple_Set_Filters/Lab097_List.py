
my_list = [1, 2, 3, 4, 5]

print("element at  the index 0 -", my_list[0])
print("element at  the index 1 -", my_list[1])
print("element at  the index 2 -", my_list[2])
print("element at  the index 3 -", my_list[3])
print("element at  the index 4 -", my_list[4])


#append()- # Append object to the end of the list.
my_list.append(4)
my_list.append(4777)
print(my_list)

# extend() _appned a new list
my_list.extend([1, 2, 3, 4, 5777])
print(my_list)

#insert()
my_list.insert(4, "vikky4")
print(my_list)
print(len(my_list))

my_list.insert(4, "vikky4")
print(my_list)
print(len(my_list))

my_list [1]= "stupid"
print(my_list)

#remove()
my_list.remove("stupid")
print(my_list)
print(len(my_list))

print("___")
print("---")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)


my_copy_list.remove("vikky4")
my_list.remove("vikky4")

my_copy_list.remove("vikky4")
my_list.remove("vikky4")

print(my_list)

my_copy_list.sort()
print(my_copy_list)

my_list.clear()
print(my_list)

