len = int(input('Введите размер списка: '))
list = []
count = 0

while count <= len:
    tmp = int(input(f'Введите значение, для элемента списка, с индексом {count}: \n'))
    list.append(tmp)
    count +=1

print(f'\nЗаполненный список: {list}')

sum = 0

for i in range(0, len):
    if i % 2 != 0:
        sum += list[i]

print(f'\nСумма элементов списка на нечетных позициях, равна {sum}')