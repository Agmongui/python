import itertools
count = 0
slovo = "НАСТЯ"
for a in itertools.product(slovo, repeat = 6):
    b = ''.join(a)
    if b.count("А") <= 1 and b.count("Я") <= 1:
        count+= 1
print(count)
