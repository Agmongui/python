from abc import ABC, abstractmethod

class Venicle(ABC):
    def __init__(self, fuel_consumption_per_100km, fuel_price):
        self._fuel_consumption_per_100km = fuel_consumption_per_100km
        self._fuel_price = fuel_price

    # Managed-атрибуты через @property
    @property
    def fuel_consumption_per_100km(self):
        return self._fuel_consumption_per_100km

    @fuel_consumption_per_100km.setter
    def fuel_consumption_per_100km(self, value):
        if value <= 0:
            raise ValueError("Расход топлива должен быть положительным числом.")
        self._fuel_consumption_per_100km = value

    @property
    def fuel_price(self):
        return self._fuel_price

    @fuel_price.setter
    def fuel_price(self, value):
        if value <= 0:
            raise ValueError("Цена топлива должна быть положительным числом.")
        self._fuel_price = value

    # Абстрактные методы
    @abstractmethod
    def calculate_fuel_consumption(self, distance, load=0):
        pass

    @abstractmethod
    def calculate_trip_cost(self, distance, load=0):
        pass

    @abstractmethod
    def calculate_trip_time(self, distance, average_speed):
        pass

    # Dunder-методы
    def __str__(self):
        return f"{self.__class__.__name__} с расходом {self.fuel_consumption_per_100km} л/100км"

    def __repr__(self):
        return f"{self.__class__.__name__}(fuel_consumption_per_100km={self.fuel_consumption_per_100km}, fuel_price={self.fuel_price})"