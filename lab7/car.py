from .Venicle import Venicle

class Car(Venicle):
    def calculate_fuel_consumption(self, distance, load=0):
        return (distance / 100) * self.fuel_consumption_per_100km

    def calculate_trip_cost(self, distance, load=0):
        fuel_consumed = self.calculate_fuel_consumption(distance)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed