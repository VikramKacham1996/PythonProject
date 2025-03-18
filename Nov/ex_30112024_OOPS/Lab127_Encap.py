class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name: " + self.name)
        print("Starting a car with the make: " + self.make)
        print("Starting a car with the model: " + self.model)


# Creating instances of the Car class
lambo = Car("Lambo", "V6", "5")
lambo.start_engine()
print("_____")
mg_hector = Car("Hector", "1.5 Turbo", "2024")
mg_hector.start_engine()
