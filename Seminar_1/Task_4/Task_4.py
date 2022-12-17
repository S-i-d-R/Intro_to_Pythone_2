quarter_num = int(input('Введите номер четверти: '))
if quarter_num == 1:
   print('x > 0 and y > 0')
elif quarter_num == 2:
   print('x < 0 and y > 0')
elif quarter_num == 3:
   print('x < 0 and y < 0')
elif quarter_num == 4:
   print('x > 0 and y < 0')
else:
   print('Такой четверти, не существует!')