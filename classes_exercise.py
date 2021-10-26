




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
            fare = 0

        elif 18 >= age <= 60:
            fare = 5

        elif age > 60:
            fare = 0

        return fare


this_car = Vehicle()
# this_car.vroom()

this_car = Bus()
print(f"The fare of the bus ride is ${this_car.fare(12)}")

