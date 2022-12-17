coordinate_x = float(input('Введите координату x: ')) 
coordinate_y = float(input('Введите координату y: '))
if coordinate_x > 0 and coordinate_y > 0:
    print('Точка находится в 1-й четверти.')
elif coordinate_x < 0 and coordinate_y > 0:
    print('Точка находится во 2-й четверти.')
elif coordinate_x < 0 and coordinate_y < 0:
    print('Точка находится в 3-й четверти.')
elif coordinate_x > 0 and coordinate_y < 0:
    print('Точка находится в 4-й четверти.')
else:
    print('Точка не соответствует, условию задачи!')