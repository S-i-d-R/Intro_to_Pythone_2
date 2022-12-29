n = int(input('Введите число N: '))

list_prod = []
prod = 1
for i in range(1, n + 1):
    prod *= i
    print(prod, end = ' ')

print()
list_fact = []