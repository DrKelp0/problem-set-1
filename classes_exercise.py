




class Vehicle:
    """Thing used for transport

    Attributes:
        name: str
        max_speed: int
        capacity: int
    """

    def __init__(self):
        self.name = "Tonymobile"
        self.max_speed = 300
        self.capacity = 100

    # def vroom(self):
    #     for max_speed in range(300):
    #         print("vroom")

class Bus(Vehicle):
    """A vehicle that is very large and carries
      passengers

    Attributes:
        fare: Cost of riding the bus
    """

    def fare(self, age: float) -> None:

        if age <= 17:
            print("The fare of the bus ride is $0")

        elif age >= 18 and age <= 60:
            print("The fare of the bus ride is $5")

        elif age > 60:
            print("The fare of the bus ride is $0")


this_car = Vehicle()
# this_car.vroom()

this_car = Bus()
this_car.fare(60)
# print(f"The fare of the bus ride is ${this_car.fare(12)}")

