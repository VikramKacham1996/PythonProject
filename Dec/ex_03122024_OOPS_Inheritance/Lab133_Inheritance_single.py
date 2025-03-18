#  How to creaate a class?
# single inheritance -> 85% of the time you will  si inapi and web automation


# Creating the Father class
class Father:
    key = "2BHK"  # Attribute of the Father class

    def car(self):  # Method of the Father class
        print("Father has a Car -> Alto")
        print(f"Father's house key: {self.key}")

# Creating the Son class (inherits from Father)
class Son(Father):  # Single Inheritance
    key2 = "3BHK"  # Attribute specific to the Son class

    def suv(self):  # Method specific to the Son class
        print("Son has an SUV -> MG Hector, Black")
        print(f"Son's house key: {self.key2}")

# Creating an object of the Father class
father_obj = Father()
father_obj.car()  # Calling Father's method

# Creating an object of the Son class
son_obj = Son()  # Correctly creating an object of the Son class
son_obj.suv()    # Calling the Son's method

# Calling an inherited method from the Father class using the Son object
son_obj.car()



