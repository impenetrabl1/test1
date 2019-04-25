from abc import ABC, abstractmethod


class VehicleBuildDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_vehicle(self):
        vehicle = Vehicle()
        wheels = self.__builder.get_wheels()
        vehicle.set_wheels(wheels)
        engine = self.__builder.get_engine()
        vehicle.set_engine(engine)
        transmission = self.__builder.get_transmission()
        vehicle.set_transmission(transmission)
        return vehicle


class Vehicle:
    def __init__(self):
        self.__wheels = None
        self.__engine = None
        self.__transmission = None

    def set_wheels(self, wheels):
        self.__wheels = wheels

    def set_engine(self, engine):
        self.__engine = engine

    def set_transmission(self, transmission):
        self.__transmission = transmission

    def __str__(self):
        return "Wheels: %s, engine: %s, transmission: %s" % (self.__wheels, self.__engine, self.__transmission)


class Builder(ABC):
    @abstractmethod
    def get_wheels(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_transmission(self):
        pass


class CarBuilder(Builder):
    def get_wheels(self):
        wheels = 4
        return wheels

    def get_engine(self):
        engine = "injector"
        return engine

    def get_transmission(self):
        transmission = "auto"
        return transmission


class MotorcycleBuilder(Builder):
    def get_wheels(self):
        wheels = 2
        return wheels

    def get_engine(self):
        engine = "diesel"
        return engine

    def get_transmission(self):
        transmission = "manual"
        return transmission


if __name__ == "__main__":
    director = VehicleBuildDirector()
    car_builder = CarBuilder()
    director.set_builder(CarBuilder())
    car = director.get_vehicle()
    print(car)  # Wheels: 4, engine: injector, transmission: auto
    motorcycle_builder = MotorcycleBuilder()
    director.set_builder(MotorcycleBuilder())
    motorcycle = director.get_vehicle()
    print(motorcycle)  # Wheels: 2, engine: diesel, transmission: manual
