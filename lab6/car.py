class Car:
    def __init__(self, fuel_consumption_per_100km, fuel_price):
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price = fuel_price

    def calculate_fuel_consumption(self, distance):
        return (distance / 100) * self.fuel_consumption_per_100km

    def calculate_trip_cost(self, distance):
        fuel_consumed = self.calculate_fuel_consumption(distance)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed
