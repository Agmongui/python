# Задание 00

Составить словарь словарей и найти расстояние между городами.

## Описание 
Составила словарь словарей и нашла расстояние между ними
используя цикл и функцию нахождения расстояния.

## Решение
```
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

def c_distances(city1,city2):
    x1, y1 = sites[city1]
    x2, y2 = sites[city2]
    return (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

distances = {}
for city1 in sites:
    distances[city1] = {}
    for city2 in sites:
        if city1 != city2:
            a = c_distances(city1,city2)
            distances[city1][city2] = round(a,2)

print(distances)
```
## Скриншот
![](0.png)

# Задание 01

## Описание
Нашла площадь круга (с точностью до 4-х знаков после запятой)
Используя Т. Пифагора, определила лежит ли точка внутри того самого круга.
Аналогично для другой точки.

## Решение
```
radius = 42

S = round(radius**2 * 3.1415926,4)
print(S)

point_1 = (23, 34)

x = point_1[0]
y = point_1[1]

point1_d = (x ** 2 + y **2 )**0.5
if point1_d <= radius:
    print('True')
else:
    print('False')

point_2 = (30, 30)

point2_d = (point_2[0] ** 2 + point_2[1] **2 )**0.5
if point2_d <= radius:
    print('True')
else:
    print('False')
```

## Скриншот
![](01.png)

# Задание 02
Расставьте знаки операций "плюс", "минус", "умножение" и скобки
между числами "1 2 3 4 5" так, что бы получилось число "25".

## Описание
Расставила знаки операций между цифрами 1 2 3 4 5, чтобы получить число 25.

## Решение
```
result = ((1 + 2) * 3 - 4) * 5
print(result)
```

## Скриншот
![](02.png)

# Задание 03
Выведите на консоль с помощью индексации строки, последовательно:
   первый фильм
   последний
   второй
   второй с конца
## Описание
Используя срезы, вывела на консоль название фильмов.
## Решение
```
print(my_favorite_movies[:10])
print(my_favorite_movies[-15:])
print(my_favorite_movies[12:25])
print(my_favorite_movies[-22:-17])
```
## Скриншот
![](03.png)
# Задание 04
Создайте списки, выведите на консоль рост отца и общий рост всей семьи.
## Описание
Составила список приблизительного роста членов моей семьи, вывела на консоль рост отца и общий рост семьи.
## Решение
```
my_family = ['мама', 'папа', 'дедушка', 'бабушка']
my_family_height = [ 
    # ['имя', рост],
    ['мама',170],['папа',180],['бабушка',160],['дедушка',165],
]
summ= my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]
print("Рост отца -", my_family_height[1][1])
print("Общий рост семьи -", summ)
```
## Скриншот
![](04.png)

# Задание 05
посадите медведя (bear) между львом и кенгуру,добавьте птиц из списка birds в последние клетки зоопарка,уберите слона,в какой клетке сидит лев (lion) и жаворонок (lark).
Номера при выводе должны быть понятны простому человеку, не программисту.
## Описание
Использовала функции для добавления, удаления животных в клетки.
## Решение
```
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1,'bear')
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

print("Лев -", zoo.index('lion') + 1)
print("Жаворонок -", zoo.index('lark') + 1)
```

## Скриншот
![](05.png)

# Задание 06
распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
Три песни звучат ХХХ.XX минут
распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
А другие три песни звучат ХХХ минут

## Описание
Расчитала общее время звучания трех песен 'Halo', 'Enjoy the Silence' и 'Clean' и 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'.

## Решение
```
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

x = round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[-1][1],2)
print("Три песни звучат",x ,"минут")

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

y = round(violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress'],2)
print("А другие три песни звуечат",y ,"минут")
```

## Скриншот
![](06.png)
# Задание 07

## Описание
Составила с помощью срезов предложение по буквам .
## Решение
```
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
let1 = secret_message[0][3]
let2 = secret_message[1][9:13]
let3 = secret_message[2][5:15:2]
let4 = secret_message[3][12:6:-1]
let5 = secret_message[4][20:15:-1]
print(let1, let2, let3, let4, let5)
```
## Скриншот
![](07.png)


# Задание 08
создайте множество цветов, произрастающих в саду и на лугу,выведите на консоль все виды цветов,выведите на консоль те, которые растут и там и там,выведите на консоль те, которые растут в саду, но не растут на лугу,выведите на консоль те, которые растут на лугу, но не растут в саду
## Описание
Создала множество цветов, вывела все виды, повторяющиеся цветы и те, что растут на одном месте, но не растут на другом.
## Решение
```
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set | meadow_set)
print(garden_set & meadow_set)
print(garden_set.difference(meadow_set))
print(meadow_set.difference(garden_set))
```
## Скриншот
![](08.png)


# Задание 09
Создайте словарь цен на продкты следующего вида (писать прямо в коде),указать надо только по 2 магазина с минимальными ценами
## Описание
Создала словарь цен на печенье, конфеты, карамель, пирожное с минимальными ценами.
## Решение
```
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99}
        
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'пятерочка', 'price': 32.99}
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99}
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99}
    ]
}

print(sweets)
```

## Скриншот
![](09.png)
# Задание 10
Рассчитать на какую сумму лежит каждого товара на складе.
## Описание
Вывела стоимость каждого товара на складе.
## Решение
```
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

table_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
table1_cost = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][0]['price']
print('Стол -', store[goods['Стол']][0]['quantity'], "шт, стоимость" ,table_cost,"руб;", store[goods['Стол']][1]['quantity'], "шт, стоимость", table1_cost,"руб;")

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa1_cost = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
print("Диван -",store[goods['Диван']][0]['quantity'], 'шт, стоимость', sofa_cost,"руб;", store[goods['Диван']][1]['quantity'], "шт, стоимость", sofa1_cost, "руб;")

chair_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chair1_cost = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chair2_cost = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
print('Стул -', store[goods['Стул']][0]['quantity'], 'шт, стоимость', chair_cost,"руб;", store[goods['Стул']][1]['quantity'], 'шт, стоимость', chair1_cost,"руб;", store[goods['Стул']][2]['quantity'], "шт, стоимость", chair2_cost,"руб;")
```
## Скриншот
![](10.png)
## Используемые источники:
https://clck.ru/MfEMS
https://skillbox.ru/media/code/mnozhestva-v-python-vvodnyy-gayd-dlya-nachinayushchikh/
https://github.com/cyberspacedk/Git-commands

# Шпаргалку по работе с командами git
git clone
git add 
git status
git push
git commit -m  
