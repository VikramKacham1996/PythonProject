class Dog:
    #A
    name = None
    breed = None
    hight = None
    weight = None

    def __init__(self):
        print("i will be called")

    #B

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass
# object ref
chow_ref = Dog() 
mow_ref = Dog()


print(chow_ref.name)
print(mow_ref.name)



