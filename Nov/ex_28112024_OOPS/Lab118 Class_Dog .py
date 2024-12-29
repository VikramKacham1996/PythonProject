class Dog:
    #A
    name = None
    breed = None
    hight = None
    weight = None

    #B
    def bark(self):
        print("Barking")
    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass
# object ref
chow = Dog()
#Dog() - Object
#chow -> Object Ref.

mow = Dog()
bow = Dog()
rancho = Dog()