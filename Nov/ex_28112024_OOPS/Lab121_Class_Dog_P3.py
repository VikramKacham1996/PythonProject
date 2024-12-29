#take i/p and create a cls in python

class Person:

    def __init__(self):
        print("i will be called")
        self.name = input("enter the name\n")
        self.age = input("enter the age\n")
        self.phone = input("enter the phone\n")
        self.occupation = input("enter the occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"Age is{self.age}",f"phone is {self.phone}",
              f"occupation is {self.occupation}")


person1 = Person()
person1.name_of_the_function_to_display()


