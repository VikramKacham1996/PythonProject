from abc import ABC, abstractmethod


class GearBox(ABC):
    @abstractmethod
    def set_gear(self):
        pass


class Engine(GearBox):
    @abstractmethod
    def start(self):
        print("Setting gear in Engine start")
        super().set_gear()

    @abstractmethod
    def stop(self):
        pass


class Car(Engine):
    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    def set_gear(self):
        print("Gearbox is ready")

    def drive(self):
        self.set_gear()
        self.start()
        self.stop()


# Instantiate and use the Car class
car_obj = Car()
car_obj.drive()
