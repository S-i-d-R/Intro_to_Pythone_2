number = int(input('Введите число N: '))
number_list = {}
sum = 0
for i in range(1, number + 1):
    number_list[i] = round((1+(1/i))** i, 3)
    sum += number_list[i]
print(number_list)
print(f'Сумма значений словаря = {round(sum,3)}')