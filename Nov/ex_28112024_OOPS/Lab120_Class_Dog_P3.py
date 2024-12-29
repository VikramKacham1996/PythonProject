class Dog:
    #A -instance variables/ data variables
    name = None
    breed = None
    hight = None
    weight = None

    def __init__(self,name, breed):
        print("PC")
        self.name = name
        self.breed = breed


    #B

    def sleep(self):
        print("who is Sleeping"+self.name)

    def talk(self):
        pass
# object ref
chow_ref = Dog("chow","mastiff")
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))

mow_ref = Dog("mow","husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))







