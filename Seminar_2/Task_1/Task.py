num = input('Введите вещественное число N: ')
digit_sum = 0
for i in num:
    if i.isdigit():
        digit_sum += int(i)
print(f'Сумма цифр числа {num} равна {digit_sum}.')