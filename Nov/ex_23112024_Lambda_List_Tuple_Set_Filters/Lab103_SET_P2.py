set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

my_set = set1.union(set2)
print(my_set)
# union means all items
my_set = set1.intersection(set2)
print(my_set)
# intersection means common items
#intersection() method (or the & operator) to find the common elements between two or more sets.
my_set =  set1.difference(set2)
print(my_set)
my_set =  set2.difference(set1)
print(my_set)