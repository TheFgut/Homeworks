class Transport:
    max_speed = 0
    fuel_consumption = 0
    cargo_capacity = 0
    max_passengers_count = 0


class Car(Transport):
    fuel_type = ""
    fuel_tank_capacity = 0

    def __init__(self, speed, fuel_consumption, cargo_capacity, passengers_count, fuel_tank_capacity, fuel_type = "Gas"):
        self.max_speed = speed
        self.fuel_consumption = fuel_consumption
        self.cargo_capacity = cargo_capacity
        self.max_passengers_count = passengers_count
        self.fuel_type = fuel_type
        self.fuel_tank_capacity = fuel_tank_capacity

    def __str__(self):
        return f"Car. Max speed - {int(self.max_speed)}km/h, fuel consumption - " \
               f"{self.fuel_consumption}l/100km, fuel type - {self.fuel_type}, fuel tank capacity - " \
               f"{self.fuel_tank_capacity}, cargo capacity - {self.cargo_capacity}kg, max passengers count -" \
               f" {self.max_passengers_count}"


class Plane(Transport):
    max_fly_height = 0
    max_ascensional_rate = 0

    def __init__(self, max_speed, fuel_consumption, cargo_capacity, max_passengers_count, max_fly_height,
                 max_ascensional_rate):
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.cargo_capacity = cargo_capacity
        self.max_passengers_count = max_passengers_count
        self.max_fly_heigth = max_fly_height;
        self.max_ascensional_rate = max_ascensional_rate

    def __str__(self):
        return f"Plane. Max speed - {int(self.max_speed)}km/h, fuel consumption - {self.fuel_consumption}l/100km," \
               f" cargo capacity - {self.cargo_capacity}kg, max passengers count - {self.max_passengers_count}, " \
               f"max fly height -= {self.max_fly_heigth}m, ascensional rate - {self.max_ascensional_rate}m/s"


class Ship(Transport):
    draft = 0
    stability = 0

    def __init__(self, max_speed, fuel_consumption, cargo_capacity, max_passengers_count, draft, stability):
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.cargo_capacity = cargo_capacity
        self.max_passengers_count = max_passengers_count
        self.draft = draft
        self.stability = stability

    def __str__(self):
        return f"Ship. Max speed - {int(self.max_speed)}knoots, fuel consumption - {self.fuel_consumption}l/100km," \
               f" cargo capacity - {self.cargo_capacity}kg, max passengers count - {self.max_passengers_count}, " \
               f"draft - {self.draft}m, stability - {self.stability}"


def print_transport_info(transport_dict, type_of_transport):
    print(type_of_transport + "s:")
    for name, transport in transport_dict.items():
        print(f"\"{name}\". Type - {transport}")
    print("\n")


planes = {"BMW_plane": Plane(600, 20, 300, 2, 3000, 8), "Kukuruznik": Plane(490, 12, 250, 2, 2500, 6.3)}
cars = {"lada": Car(176, 7.3, 1163, 5, 43, "Gas"), "moskwich": Car(140, 8.8, 1045, 5, 46, "Gas"),
        "jiguli": Car(140, 7.4, 955, 5, 39, "Gas")}
ships = {"Small ship": Ship(10, 20, 500, 6, 3, 12), "Big ship": Ship(12, 115, 25000, 30, 15, 130)}

print_transport_info(planes, "Plane")
print_transport_info(ships, "Ship")
print_transport_info(cars, "Car")

