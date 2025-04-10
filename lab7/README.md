# Задание
Задания для самостоятельного выполнения
Перепишите свой вариант ЛР №6 с использованием классов и объектов. Задание то же, вариант GUI фреймворка возьмите следующий по списку. Для успешной сдачи в коде должны присутствовать:

использование абстрактного базового класса и соотвествующих декораторов для методов,
иерархия наследования,
managed - атрибуты,
минимум 2 dunder-метода у каждого класса.

## Решение
main
```python
from abc import ABC #импорт абстрактного класса
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from vehicles_package.car import Car
from vehicles_package.truck import Truck
from vehicles_package.bus import Bus
from docx import Document

class VehicleApp(App):
    def build(self):
        self.title = "Расчет поездки"
        return VehicleLayout()

class VehicleLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 5  # Уменьшаем расстояние между виджетами

        # Выбор типа транспорта
        self.vehicle_type = Spinner(
            text="Легковой",
            values=("Легковой", "Грузовой", "Пассажирский"),
            size_hint=(0.5, 0.05),  # Уменьшаем ширину и высоту
            pos_hint={"center_x": 0.5}  # Центрируем по горизонтали
        )
        self.add_widget(Label(text="Тип транспорта:", size_hint=(1, 0.05)))
        self.add_widget(self.vehicle_type)

        # Ввод расстояния
        self.distance_input = TextInput(
            hint_text="Расстояние (км)",
            multiline=False,
            size_hint=(0.5, 0.05),  # Уменьшаем ширину и высоту
            pos_hint={"center_x": 0.5}  # Центрируем по горизонтали
        )
        self.add_widget(Label(text="Расстояние (км):", size_hint=(1, 0.05)))
        self.add_widget(self.distance_input)

        # Ввод загрузки
        self.load_input = TextInput(
            hint_text="Загрузка",
            multiline=False,
            size_hint=(0.5, 0.05),  # Уменьшаем ширину и высоту
            pos_hint={"center_x": 0.5}  # Центрируем по горизонтали
        )
        self.add_widget(Label(text="Загрузка:", size_hint=(1, 0.05)))
        self.add_widget(self.load_input)

        # Кнопка расчета
        calculate_button = Button(
            text="Рассчитать",
            size_hint=(0.5, 0.05),  # Уменьшаем ширину и высоту
            pos_hint={"center_x": 0.5}  # Центрируем по горизонтали
        )
        calculate_button.bind(on_press=self.calculate)
        self.add_widget(calculate_button)

        # Результат
        self.result_label = Label(
            text="Результат:",
            size_hint=(1, 0.2),  # Оставляем больше места для результата
            halign="center",
            valign="middle"
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))  # Для переноса текста
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            vehicle_type = self.vehicle_type.text
            distance = float(self.distance_input.text)
            load = float(self.load_input.text)

            if vehicle_type == "Легковой":
                vehicle = Car(fuel_consumption_per_100km=8, fuel_price=50)
            elif vehicle_type == "Грузовой":
                vehicle = Truck(fuel_consumption_per_100km=15, fuel_price=50, load_capacity=10)
            elif vehicle_type == "Пассажирский":
                vehicle = Bus(fuel_consumption_per_100km=12, fuel_price=50, passenger_capacity=50)
            else:
                raise ValueError("Выберите тип транспорта.")

            fuel = vehicle.calculate_fuel_consumption(distance, load)
            cost = vehicle.calculate_trip_cost(distance, load)
            time = vehicle.calculate_trip_time(distance, average_speed=60)

            result = f"Расход топлива: {fuel:.2f} л\nСтоимость: {cost:.2f} руб.\nВремя: {time:.2f} ч"
            self.result_label.text = result
        except Exception as e:
            self.show_popup("Ошибка", str(e))

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()

if __name__ == "__main__":
    VehicleApp().run()
```
venicle
```python
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
```

car
```python
from .Venicle import Venicle

class Car(Venicle):
    def calculate_fuel_consumption(self, distance, load=0):
        return (distance / 100) * self.fuel_consumption_per_100km

    def calculate_trip_cost(self, distance, load=0):
        fuel_consumed = self.calculate_fuel_consumption(distance)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed
```
bus
```python
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
```
truck
```python
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

    # Дополнительные dunder-методы
    def __eq__(self, other):
        if isinstance(other, Truck):
            return (
                self.fuel_consumption_per_100km == other.fuel_consumption_per_100km and
                self.fuel_price == other.fuel_price and
                self.load_capacity == other.load_capacity
            )
        return False
```

## Скриншот
![image](https://github.com/user-attachments/assets/ba909aec-77d1-4c06-a3bd-304a56528956)

## Список литературы
[chatgpt](https://chatgpt.com/?)

[dunder](https://tproger.ru/articles/dunder-metody-zachem-oni-nuzhny-i-chto-mogut)
