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
