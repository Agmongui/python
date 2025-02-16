x = 16**18 * 4**10 - 46 - 16
s =''
while x!= 0:
    s += str(x % 4)
    x //= 4
s = s[::-1]
print(s.count("3"))