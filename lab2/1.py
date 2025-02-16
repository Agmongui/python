len = "НАСТЯ"
count = 0
for l1 in len:
    for l2 in len:
        for l3 in len:
            for l4 in len:
                for l5 in len:
                    for l6 in len:
                        x = l1 + l2 + l3 + l4 +l5 + l6
                        if x.count("А") <= 1 and x.count("Я") <= 1:
                            count += 1
print(count)
