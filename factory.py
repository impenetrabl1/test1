class Vehicle:
    @staticmethod
    def factory(tires):
        if tires == 4:
            return Car()
        if tires == 2:
            return Motorcycle()


class Car(Vehicle):
    def __init__(self):
        self.__tires = 4
        self.__engine = "injector"
        self.__transmission = "auto"

    def __str__(self):
        return "Tires: %s, engine: %s, transmission: %s" % (self.__tires, self.__engine, self.__transmission)


class Motorcycle(Vehicle):
    def __init__(self):
        self.__tires = 2
        self.__engine = "diesel"
        self.__transmission = "manual"

    def __str__(self):
        return "Tires: %s, engine: %s, transmission: %s" % (self.__tires, self.__engine, self.__transmission)


if __name__ == "__main__":
    car = Vehicle.factory(4)
    print(car)  # Tires: 4, engine: diesel, transmission: manual
    motorcycle = Vehicle.factory(2)
    print(motorcycle)  # Tires: 2, engine: injector, transmission: auto
