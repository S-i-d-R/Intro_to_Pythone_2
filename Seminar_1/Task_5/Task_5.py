import math

coordinate_x1 = float(input('Введите координату x, первой точки: '))
coordinate_y1 = float(input('Введите координату y, первой точки: '))
coordinate_x2 = float(input('Введите координату x, второй точки: '))
coordinate_y2 = float(input('Введите координату y, второй точки: '))
distance = round(math.sqrt((coordinate_x2 - coordinate_x1) ** 2 + (coordinate_y2 - coordinate_y1) ** 2), 2)
print('Расстояние, между первой и второй точкой:', distance)