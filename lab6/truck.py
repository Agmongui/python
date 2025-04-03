class Truck:
    def __init__(self, fuel_consumption_per_100km, fuel_price, load_capacity):
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price = fuel_price
        self.load_capacity = load_capacity

    def calculate_fuel_consumption(self, distance, load):
        # Увеличиваем расход топлива на 10% за каждую тонну загрузки
        adjusted_consumption = self.fuel_consumption_per_100km * (1 + (load / self.load_capacity) * 0.1)
        return (distance / 100) * adjusted_consumption

    def calculate_trip_cost(self, distance, load):
        fuel_consumed = self.calculate_fuel_consumption(distance, load)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed