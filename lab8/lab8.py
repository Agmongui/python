import wx
import wx.grid
import calendar
from datetime import datetime


class CalendarApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(CalendarApp, self).__init__(*args, **kwargs)

        # Настройка окна
        self.SetTitle("Календарь с событиями")
        self.SetSize(800, 600)
        self.Centre()

        # Инициализация переменных
        self.now = datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.events = {}  # Хранилище событий (ключ: дата в формате YYYY-MM-DD, значение: список событий)

        # Создание панели и элементов интерфейса
        self.panel = wx.Panel(self)
        self.create_widgets()

    def create_widgets(self):
        # Выбор года
        year_label = wx.StaticText(self.panel, label="Год:", pos=(20, 20))
        self.year_input = wx.TextCtrl(self.panel, value=str(self.year), pos=(70, 20), size=(80, -1))

        # Выбор месяца
        month_label = wx.StaticText(self.panel, label="Месяц:", pos=(180, 20))
        self.month_input = wx.TextCtrl(self.panel, value=str(self.month), pos=(240, 20), size=(80, -1))

        # Кнопка для обновления календаря
        update_button = wx.Button(self.panel, label="Показать календарь", pos=(340, 20))
        update_button.Bind(wx.EVT_BUTTON, self.show_calendar)  # Привязываем обработчик

        # Сетка для отображения календаря
        self.calendar_grid = wx.grid.Grid(self.panel, pos=(20, 60), size=(740, 300))  # Создаем сетку
        self.calendar_grid.CreateGrid(6, 7)  # 6 строк (недель), 7 столбцов (дней недели)
        self.calendar_grid.SetRowLabelSize(0)  # Убираем метки строк
        self.calendar_grid.SetColLabelValue(0, "Пн")
        self.calendar_grid.SetColLabelValue(1, "Вт")
        self.calendar_grid.SetColLabelValue(2, "Ср")
        self.calendar_grid.SetColLabelValue(3, "Чт")
        self.calendar_grid.SetColLabelValue(4, "Пт")
        self.calendar_grid.SetColLabelValue(5, "Сб")
        self.calendar_grid.SetColLabelValue(6, "Вс")

        # Привязываем обработчик клика по ячейке
        self.calendar_grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click)

        # Поле для ввода даты события
        date_label = wx.StaticText(self.panel, label="Дата (YYYY-MM-DD):", pos=(20, 400))
        self.date_input = wx.TextCtrl(self.panel, pos=(150, 400), size=(120, -1))

        # Поле для ввода события
        event_label = wx.StaticText(self.panel, label="Событие:", pos=(290, 400))
        self.event_input = wx.TextCtrl(self.panel, pos=(350, 400), size=(200, -1))

        # Кнопка для добавления события
        add_event_button = wx.Button(self.panel, label="Добавить событие", pos=(570, 400))
        add_event_button.Bind(wx.EVT_BUTTON, self.add_event)

        # Текстовое поле для отображения событий
        self.events_text = wx.TextCtrl(
            self.panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL,
            pos=(20, 440),
            size=(740, 120)
        )

    def show_calendar(self, event):
        """Обновление календаря."""
        try:
            # Получение выбранных года и месяца
            year = int(self.year_input.GetValue())
            month = int(self.month_input.GetValue())

            if not (1900 <= year <= 2100) or not (1 <= month <= 12):
                raise ValueError("Некорректные значения года или месяца.")

            # Очистка предыдущего календаря
            for row in range(6):
                for col in range(7):
                    self.calendar_grid.SetCellValue(row, col, "")
                    self.calendar_grid.SetCellBackgroundColour(row, col, wx.WHITE)  # Сброс цвета

            # Генерация календаря
            cal = calendar.monthcalendar(year, month)

            # Заполнение сетки днями месяца
            for row, week in enumerate(cal):
                for col, day in enumerate(week):
                    if day != 0:
                        date_key = f"{year}-{month:02d}-{day:02d}"  # Формат даты YYYY-MM-DD
                        self.calendar_grid.SetCellValue(row, col, str(day))

                        # Выделение сегодняшней даты
                        if year == self.now.year and month == self.now.month and day == self.now.day:
                            self.calendar_grid.SetCellBackgroundColour(row, col, wx.GREEN)  # Выделение зеленым цветом

                        # Отображение событий, если они есть
                        if date_key in self.events:
                            events_list = self.events[date_key]
                            events_summary = "\n".join(events_list[:2])  # Показываем максимум 2 события
                            self.calendar_grid.SetCellValue(row, col, f"{day}\n{events_summary}")

        except ValueError as e:
            wx.MessageBox(f"Ошибка: {e}", "Ошибка", wx.OK | wx.ICON_ERROR)

    def on_cell_click(self, event):
        """Обработчик клика по ячейке сетки."""
        row = event.GetRow()  # Получаем строку
        col = event.GetCol()  # Получаем столбец

        # Получаем значение ячейки (день месяца)
        day = self.calendar_grid.GetCellValue(row, col).strip()

        if day.isdigit():  # Проверяем, что в ячейке есть число
            day = int(day)
            year = int(self.year_input.GetValue())
            month = int(self.month_input.GetValue())

            # Формируем ключ даты в формате YYYY-MM-DD
            date_key = f"{year}-{month:02d}-{day:02d}"

            # Проверяем, есть ли события для этой даты
            if date_key in self.events:
                events_list = self.events[date_key]
                events_message = "\n".join([f"{idx}. {event}" for idx, event in enumerate(events_list, start=1)])
                wx.MessageBox(f"События на {date_key}:\n{events_message}", "События", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox(f"На {date_key} нет событий.", "События", wx.OK | wx.ICON_INFORMATION)

        event.Skip()  # Пропускаем дальнейшую обработку события

    def add_event(self, event):
        """Добавление события."""
        try:
            # Получение даты и события
            date = self.date_input.GetValue()
            event_description = self.event_input.GetValue()

            # Проверка корректности даты
            datetime.strptime(date, "%Y-%m-%d")

            if not event_description.strip():
                raise ValueError("Описание события не может быть пустым.")

            # Добавление события в хранилище
            if date not in self.events:
                self.events[date] = []  # Создаем пустой список, если дата еще не существует
            self.events[date].append(event_description)  # Добавляем событие в список

            # Обновление текстового поля с событиями
            self.update_events_display()

            # Очистка полей ввода
            self.date_input.Clear()
            self.event_input.Clear()
        except ValueError as e:
            wx.MessageBox(f"Ошибка: {e}", "Ошибка", wx.OK | wx.ICON_ERROR)

    def update_events_display(self):
        """Обновление текстового поля с событиями."""
        events_output = "События:\n"
        for date, events_list in self.events.items():
            events_output += f"{date}:\n"
            for idx, event in enumerate(events_list, start=1):
                events_output += f"  {idx}. {event}\n"
        # Отображение событий в текстовом поле
        self.events_text.SetValue(events_output)


# Запуск приложения
if __name__ == "__main__":
    app = wx.App(False)
    frame = CalendarApp(None)
    frame.Show()
    app.MainLoop()