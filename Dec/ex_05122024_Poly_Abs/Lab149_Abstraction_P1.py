# abstraction
# hide the details and show what is required.


# car -with key _ __private ,tyres ->public,

# car -> multiple -Engine, GearBox
# car -> driver ->Engine , gearbox?

from abc import ABC, abstractmethod



class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Bark Bark....")

obj_dog = Dog("chintu")
obj_dog.make_sound()