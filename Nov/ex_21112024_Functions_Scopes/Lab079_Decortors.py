
def add_extra_secuirty(func):
    def wrapper():
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcash, Gloves, Knee guards, License")
        func() #driving_Scooty()
        print("3. After the function is called")
        print("4. Secure Driving, leave the items")

    return wrapper()

@add_extra_secuirty
def driving_zest110_Scooty():
    print("Zest110")



@add_extra_secuirty
def driving_Scooty():
    print("Normal Function!!")
    print("I am driving Scooty")




def add_extra_secuirty(func):
    def wrapper():
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcash, Gloves, Knee guards, License")
        func()  # Call the original function
        print("3. After the function is called")
        print("4. Secure Driving, leave the items")

    return wrapper  # Return the wrapper function itself

@add_extra_secuirty
def driving_zest110_Scooty():
    print("Zest110")

@add_extra_secuirty
def driving_Scooty():
    print("Normal Function!!")
    print("I am driving Scooty")

# Call the functions
driving_zest110_Scooty()
driving_Scooty()
