pool = 121

count = 1
while pool >= 0:
    if count == 1:
        move1 = int(input("Ход Игрока №1: "))
        if move1 < 1 or move1 > 28:
            print ("Возьмите от 1 до 28 конфет!")
        elif move1 > pool:
            print (f"Возьмите от 1 до {pool} конфет!")
        else:
            pool -= move1
            print (f"Осталось {pool} конфет.")
            count -= 1
    elif count == 0:
        move2 = int(input("Ход Игрока №2: "))
        if move2 < 1 or move2 > 28:
            print ("Возьмите от 1 до 28 конфет!")
        elif move2 > pool:
            print (f"Возьмите от 1 до {pool} конфет!")
        else:
            pool -= move2
            print (f"Осталось {pool} конфет.")
            count += 1
if count == 0:
    print ("Все конфеты достаются Игорку №1")
else:
    print ("Все конфеты достаются Игорку №2")    