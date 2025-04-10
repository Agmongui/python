from .Venicle import Venicle

class Bus(Venicle):
    def __init__(self, fuel_consumption_per_100km, fuel_price, passenger_capacity):
        super().__init__(fuel_consumption_per_100km, fuel_price)
        self._passenger_capacity = passenger_capacity

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @passenger_capacity.setter
    def passenger_capacity(self, value):
        if value <= 0:
            raise ValueError("Вместимость должна быть положительным числом.")
        self._passenger_capacity = value

    def calculate_fuel_consumption(self, distance, passengers=0):
        adjusted_consumption = self.fuel_consumption_per_100km * (1 + (passengers / self.passenger_capacity) * 0.05)
        return (distance / 100) * adjusted_consumption

    def calculate_trip_cost(self, distance, passengers=0):
        fuel_consumed = self.calculate_fuel_consumption(distance, passengers)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed