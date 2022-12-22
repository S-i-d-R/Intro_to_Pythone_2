lis = [1, 1, 2, 4, 5, 6, 7, 7, 8]
lis1 = []
for i in lis:
    if lis.count(i) < 2:
        lis1.append(i)

print(lis1)