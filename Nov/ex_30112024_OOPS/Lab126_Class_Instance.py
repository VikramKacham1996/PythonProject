class Person:
    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name
amit = Person("amit")
vikram = Person("vikram")

print(amit.name)
print(vikram.name)
print("who is walking",amit.walk())
print("who is walking" ,vikram.walk())
