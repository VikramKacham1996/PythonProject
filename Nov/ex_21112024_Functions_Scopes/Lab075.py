pb_global_b = 10

def pb_func():
    pb_a = 11
    print(pb_a)
    print(pb_global_b)


#print(pb_a) // name 'pb_a' is not defined
print(pb_global_b)  # acting like global variable.

pb_func()




