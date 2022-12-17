num = int(input("Введите номер дня недели: "))
if num > 0 and num < 6:
    print("Это будний день.")
if num > 5 and num < 8:
    print("Это выходной день.")
if num > 7 or num < 1:
    print("Такого номера дня недели, не существует!")