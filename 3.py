def F(n): 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + n // i
    return 0
k = 0
for i in range(452021 + 1, 10000000000000):
    if F(i) % 7 == 3:
        print(i, F(i))
        k += 1
    if k == 5: 
        break