# Задание
Реализуйте приложение с GUI (приложения-игры допускается делать с использованием TUI-пакетов) по своему варианту. Можно изменить задание на собственную тему, согласовав с преподавателем. Требования:

приложение должно быть написано с применением ОО парадигмы
исключительные ситуации должны обрабатываться с использованием собственных исключений
GUI/TUI фреймворки не должны повторяться в группе

## Объяснение
Написала код GUI - WxPython, календарь, чтобы можно было вводить одни или несколько событий на определнный день.

## Решение
```python
import wx
import wx.grid
import calendar
from datetime import datetime


class CalendarApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(CalendarApp, self).__init__(*args, **kwargs) # приватные атрибуты  ( не должны использоваться напрямую)
        self._now = datetime.now()
        self._year = self._now.year
        self._month = self._now.month
        self._events = {}  # Хранилище событий (ключ: дата в формате YYYY-MM-DD, значение: список событий)

        # Создание панели и элементов интерфейса
        self._panel = wx.Panel(self)
        self.create_widgets()

    def create_widgets(self):
        """Создание общих виджетов."""
    # Выбор года
        year_label = wx.StaticText(self._panel, label="Год:", pos=(20, 20))
        self._year_input = wx.TextCtrl(self._panel, value=str(self._year), pos=(70, 20), size=(80, -1))

        # Выбор месяца
        month_label = wx.StaticText(self._panel, label="Месяц:", pos=(180, 20))
        self.month_input = wx.TextCtrl(self._panel, value=str(self._month), pos=(240, 20), size=(80, -1))

        # Кнопка для обновления календаря
        update_button = wx.Button(self._panel, label="Показать календарь", pos=(340, 20))
        update_button.Bind(wx.EVT_BUTTON, self.show_calendar) # обновляет календарь для выбранного года и месяца

        # Сетка для отображения календаря
        self._calendar_grid = wx.grid.Grid(self._panel, pos=(20, 60), size=(740, 300))
        self._calendar_grid.CreateGrid(6, 7)
        self._calendar_grid.SetRowLabelSize(0)
        for col, day in enumerate(["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]):
            self._calendar_grid.SetColLabelValue(col, day)

        # Привязываем обработчик клика по ячейке
        self._calendar_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click)  # нажимаю на день и высвечивает событие 

        # Поле для ввода даты события
        date_label = wx.StaticText(self._panel, label="Дата (YYYY-MM-DD):", pos=(20, 400))
        self._date_input = wx.TextCtrl(self._panel, pos=(150, 400), size=(120, -1))

        # Поле для ввода события
        event_label = wx.StaticText(self._panel, label="Событие:", pos=(290, 400))
        self._event_input = wx.TextCtrl(self._panel, pos=(350, 400), size=(200, -1))

        # Кнопка для добавления события
        add_event_button = wx.Button(self._panel, label="Добавить событие", pos=(570, 400))
        add_event_button.Bind(wx.EVT_BUTTON, self.add_event) # Чтобы создать новое событие для введенной даты и обновить старый список событий

        # Текстовое поле для отображения событий
        self._events_text = wx.TextCtrl(
            self._panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL,
            pos=(20, 440),
            size=(740, 120)
        )

    def on_cell_click(self, event): 
        """Обработчик клика по ячейке сетки."""
        try:
            row = event.GetRow()  # Получаем строку
            col = event.GetCol()  # Получаем столбец

            # Получаем значение ячейки (день месяца)
            day = self._calendar_grid.GetCellValue(row, col).strip()

            if not day.isdigit():  # Проверяем, что в ячейке есть число
                wx.MessageBox("Выбранная ячейка не содержит дату.", "Ошибка", wx.OK | wx.ICON_ERROR)
                event.Skip()
                return

            day = int(day)
            year = int(self._year_input.GetValue())
            month = int(self.month_input.GetValue())

            # Формируем ключ даты в формате YYYY-MM-DD
            date_key = f"{year}-{month:02d}-{day:02d}"

            # Проверяем, есть ли события для этой даты
            if date_key in self._events:
                events_list = self._events[date_key]
                events_message = "\n".join([f"{idx}. {event}" for idx, event in enumerate(events_list, start=1)])
                wx.MessageBox(f"События на {date_key}:\n{events_message}", "События", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(f"На {date_key} нет событий.", "События", wx.OK | wx.ICON_INFORMATION)

        except Exception as e:
            wx.MessageBox(f"Произошла ошибка: {e}", "Ошибка", wx.OK | wx.ICON_ERROR)

        finally:
            event.Skip()  # Пропускаем дальнейшую обработку события

    def show_calendar(self, event):
        """Обновление календаря."""
        raise NotImplementedError("Метод должен быть переопределен в подклассе.")

    def add_event(self, event): # хранилище событий
        """Добавление события."""
        try:
            # Получение даты и события
            date = self._date_input.GetValue()
            event_description = self._event_input.GetValue()

            # Проверка корректности даты
            datetime.strptime(date, "%Y-%m-%d")

            if not event_description.strip():
                raise ValueError("Описание события не может быть пустым.")

            # Добавление события в хранилище
            if date not in self._events:
                self._events[date] = []  # Создаем пустой список, если дата еще не существует
            self._events[date].append(event_description)  # Добавляем событие в список

            # Обновление текстового поля с событиями
            self.update_events_display()

            # Очистка полей ввода
            self.date_input.Clear()
            self._event_input.Clear()
        except ValueError as e:
            wx.MessageBox(f"Ошибка: {e}", "Ошибка", wx.OK | wx.ICON_ERROR)

    def update_events_display(self): # обновляет текстовое поле
        """Обновление текстового поля с событиями."""
        events_output = "События:\n"
        for date, events_list in self._events.items():
            events_output += f"{date}:\n"
            for idx, event in enumerate(events_list, start=1):
                events_output += f"  {idx}. {event}\n"
        # Отображение событий в текстовом поле
        self._events_text.SetValue(events_output)


class AdvancedCalendarApp(CalendarApp):
    def __init__(self, *args, **kwargs):
        super(AdvancedCalendarApp, self).__init__(*args, **kwargs)
        self.SetTitle("Улучшенный календарь")

    def show_calendar(self, event):
        """Переопределенный метод для отображения календаря."""
        try:
            # Получение выбранных года и месяца
            year = int(self._year_input.GetValue())
            month = int(self.month_input.GetValue())

            if not (1900 <= year <= 2100) or not (1 <= month <= 12):
                raise ValueError("Некорректные значения года или месяца.")

            # Очистка предыдущего календаря
            for row in range(6):
                for col in range(7):
                    self._calendar_grid.SetCellValue(row, col, "")
                    self._calendar_grid.SetCellBackgroundColour(row, col, wx.WHITE)  # Сброс цвета

            # Генерация календаря
            cal = calendar.monthcalendar(year, month)

            # Заполнение сетки днями месяца
            for row, week in enumerate(cal):
                for col, day in enumerate(week):
                    if day != 0:
                        date_key = f"{year}-{month:02d}-{day:02d}"  # Формат даты YYYY-MM-DD
                        self._calendar_grid.SetCellValue(row, col, str(day))

                        # Выделение сегодняшней даты
                        if year == self._now.year and month == self._now.month and day == self._now.day:
                            self._calendar_grid.SetCellBackgroundColour(row, col, wx.GREEN)  # Выделение зеленым цветом

                        # Отображение событий, если они есть
                        if date_key in self._events:
                            events_summary = "\n".join(self._events[date_key][:2])  # Показываем максимум 2 события
                            self._calendar_grid.SetCellValue(row, col, f"{day}\n{events_summary}")

        except ValueError as e:
            wx.MessageBox(f"Ошибка: {e}", "Ошибка", wx.OK | wx.ICON_ERROR)


# Запуск приложения
if __name__ == "__main__":
    app = wx.App(False)
    frame = AdvancedCalendarApp(None)  # Используем подкласс
    frame.Show()
    app.MainLoop()
```
## Скриншот
![image](https://github.com/user-attachments/assets/56964757-b2d0-4fd4-b1bd-c21c43cb3fbf)
## Список литературы
[chat.qwen.ai](https://chat.qwen.ai/c/0cb0994f-4c6c-4887-be41-0408d99a3969)
