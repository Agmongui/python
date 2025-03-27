from math import pi
def pi_digits_generator():
    for digit in str(pi).replace('.', ''):
        yield int(digit)
digits = pi_digits_generator()
values = map(lambda x: x / (x ** 2) if x != 0 else 0, digits)
result = sum(values)
print(f"Сумма: {result}")