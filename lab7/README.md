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
import tkinter as tk
from abc import ABC #импорт абстрактного класса
from tkinter import filedialog
from tkinter import messagebox
from vehicles_package.car import Car
from vehicles_package.truck import Truck
from vehicles_package.bus import Bus
from docx import Document

class VenicleApp(ABC):
    def __init__(self, root):
        self.root = root
        self.root.title("Расчет поездки")
        self.root.geometry("400x350")

        tk.Label(root, text="Тип транспорта:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.vehicle_type = tk.StringVar(value="Легковой")
        tk.OptionMenu(root, self.vehicle_type, "Легковой", "Грузовой", "Пассажирский").grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Расстояние (км):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.distance_input = tk.Entry(root)
        self.distance_input.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Загрузка:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.load_input = tk.Entry(root)
        self.load_input.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(root, text="Рассчитать", command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Результат:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.result_text = tk.Text(root, height=5, width=40)
        self.result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def calculate(self):
        try:
            vehicle_type = self.vehicle_type.get()
            distance = float(self.distance_input.get())
            load = float(self.load_input.get())


            if vehicle_type == "Легковой":
                vehicle = Car(fuel_consumption_per_100km=8, fuel_price=50)
                fuel = vehicle.calculate_fuel_consumption(distance)
                cost = vehicle.calculate_trip_cost(distance)
                time = vehicle.calculate_trip_time(distance, average_speed=60)
            elif vehicle_type == "Грузовой":
                vehicle = Truck(fuel_consumption_per_100km=15, fuel_price=50, load_capacity=10)
                fuel = vehicle.calculate_fuel_consumption(distance, load)
                cost = vehicle.calculate_trip_cost(distance, load)
                time = vehicle.calculate_trip_time(distance, average_speed=50)
            elif vehicle_type == "Пассажирский":
                vehicle = Bus(fuel_consumption_per_100km=12, fuel_price=50, passenger_capacity=50)
                fuel = vehicle.calculate_fuel_consumption(distance, load)
                cost = vehicle.calculate_trip_cost(distance, load)
                time = vehicle.calculate_trip_time(distance, average_speed=60)
            else:
                raise ValueError("Выберите тип транспорта.")

            result = f"Расход топлива: {fuel:.2f} л\nСтоимость: {cost:.2f} руб.\nВремя: {time:.2f} ч"
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
        self.save_report(fuel, cost, time)
            

    def save_report(self, fuel, cost, time):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Word Document", "*.docx")],
                title="Сохранить отчет"
            )
            if not file_path:
                return  
            doc = Document()
            doc.add_heading("Отчет по поездке", level=1)
            doc.save("C:\domashka\op\питон\lab06\Отчёт.docx")
            messagebox.showinfo("Готово", f"Отчет сохранен в файл: {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить отчет: {e}")
    
    def __str__(self):
        """Строковое представление объекта для удобного вывода."""
        return f"VehicleApp: Тип транспорта={self.vehicle_type.get()}, Расстояние={self.distance_input.get()} км, Загрузка={self.load_input.get()}"

    def __repr__(self):
        """Формальное строковое представление объекта для отладки."""
        return f"VehicleApp(vehicle_type={self.vehicle_type.get()}, distance={self.distance_input.get()}, load={self.load_input.get()})"
if __name__ == "__main__":
    root = tk.Tk()
    app = VenicleApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = VenicleApp(root)
    root.mainloop()
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
![image](https://github.com/user-attachments/assets/78d0b192-20f1-4ed6-94ad-af443da3b6bf)
## Список литературы
[chatgpt](https://chatgpt.com/?)
[dender](https://tproger.ru/articles/dunder-metody-zachem-oni-nuzhny-i-chto-mogut)
