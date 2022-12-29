n = int(input('Введите число N: '))

list_n = []
for i in range(-abs(n), abs(n) + 1):
    list_n.append(i)
print(list_n)

prod = 1
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        prod *= list_n[int(line)]
    print(prod)