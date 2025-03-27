## Задание 1
Замыкание, отбирающее только уникальные значения из переданных.
Декоратор, который будет ограничивать количество вызовов функций.
# Описание
Создала декеоратор, который огарничивает количество вызовов и замыкание, которое отбирает только уникальные значения из переданных
Решение 
``` python
def limit_calls(max_calls):
    def decorator(func):
        func.calls = 0
        def wrapper(*args, **kwargs):
            if func.calls >= max_calls:
                raise ValueError(f"Функция {func.__name__} была вызвана больше {max_calls} раз.")
            func.calls += 1
            return func(*args, **kwargs)       
        return wrapper
    return decorator

def unique_values():
    seen = set()
    def inner(values):
        return [value for value in values if value not in seen and not seen.add(value)]
    return inner
unique_values_limited = limit_calls(4)(unique_values())

print(unique_values_limited([1, 2, 2, 3]))  
print(unique_values_limited([4, 5, 5, 6]))  
print(unique_values_limited([7, 8, 9]))     
print(unique_values_limited([1, 2, 3]))     
#print(unique_values_limited([1, 2, 3]))
```
# Скриншот
![](image.png)
# Список литературы
[Уникальное значение](https://sky.pro/media/poluchenie-unikalnyh-znachenij-iz-spiska-v-python/)
[Декоратор](https://habr.com/ru/companies/otus/articles/727590/)
[Замыкание](https://habr.com/ru/articles/781866/)