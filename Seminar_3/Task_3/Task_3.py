list = [1.1, 1.2, 3.1, 5.1, 10.01]

for i in range(len(list)):
    list[i] -= int(list[i])

    print(round(max(list) - min(list),2))