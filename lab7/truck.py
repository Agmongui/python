from .Venicle import Venicle

class Truck(Venicle):
    def __init__(self, fuel_consumption_per_100km, fuel_price, load_capacity):
        super().__init__(fuel_consumption_per_100km, fuel_price)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        self._load_capacity = value

    def calculate_fuel_consumption(self, distance, load=0):
        adjusted_consumption = self.fuel_consumption_per_100km * (1 + (load / self.load_capacity) * 0.1)
        return (distance / 100) * adjusted_consumption

    def calculate_trip_cost(self, distance, load=0):
        fuel_consumed = self.calculate_fuel_consumption(distance, load)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed

