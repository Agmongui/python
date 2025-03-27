## Задание 
Генератор цифр числа π. Поделите каждую цифру на её квадрат и найдите сумму этих значений.
# Описание
Написала код, который находит сумму значений, деленные на ее квадрат.
Использовала функцию map.
# Решение
```python
from math import pi
def pi_digits_generator():
    for digit in str(pi).replace('.', ''):
        yield int(digit)
digits = pi_digits_generator()
values = map(lambda x: x / (x ** 2) if x != 0 else 0, digits)
result = sum(values)
print(f"Сумма: {result}")
```
# Скриншот
![](image.png)