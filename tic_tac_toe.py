def tic_tac_toe():
    field = [[' ', ' ', ' '] for i in range(3)]

    def great():
        print('-------------------')
        print(' Приветствуем вас  ')
        print('      В игре       ')
        print('  крестики-нолики  ')
        print('-------------------')
        print(' формат ввода: x y ')
        print(' x - номер строки  ')
        print(' y - номер столбца ')

    def show():  # Вывод игрового поля
        print()
        print('    | 0 | 1 | 2 | ')
        print('  ---------------')
        for i, row in enumerate(field):
            row_str = f'  {i} | {" | ".join(row)} | '
            print(row_str)
            print('  ---------------')
        print()

    def ask():  # Ввод пользователя + проверки правильности ввода
        while True:
            cords = input('     Ваш ход: ').split()

            if len(cords) != 2:
                print(' Введите две координаты! ')
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(' Введите числа! ')
                continue

            x, y = int(x), int(y)

            if 0 > x or x > 2 or 0 > y or y > 2:
                print(' Координаты вне диапазона! ')
                continue

            if field[x][y] != ' ':
                print(' Клетка занята! ')
                continue
            return x, y

    def check_win():  # Проверка выигрышных комбинаций. Отдельно проверяем каждую выигрышную комбинацию

        for i in range(3):
            symbols = []
            for j in range(3):
                symbols.append(field[i][j])
            if symbols == ['X', 'X', 'X']:
                return True, 'Крестики победили!!!'

        for i in range(3):
            symbols = []
            for j in range(3):
                symbols.append(field[j][i])
            if symbols == ['X', 'X', 'X']:
                return True, 'Крестики победили!!!'

        symbols = []
        for i in range(3):
            symbols.append(field[i][i])
        if symbols == ['X', 'X', 'X']:
            return True, 'Крестики победили!!!'

        symbols = []
        for i in range(3):
            symbols.append(field[i][2 - i])
        if symbols == ['X', 'X', 'X']:
            return True, 'Крестики победили!!!'

        for i in range(3):
            symbols = []
            for j in range(3):
                symbols.append(field[i][j])
            if symbols == ['0', '0', '0']:
                return True, 'Нолики победили!!!'

        for i in range(3):
            symbols = []
            for j in range(3):
                symbols.append(field[j][i])
            if symbols == ['0', '0', '0']:
                return True, 'Нолики победили!!!'

        symbols = []
        for i in range(3):
            symbols.append(field[i][i])
        if symbols == ['0', '0', '0']:
            return True, 'Нолики победили!!!'

        symbols = []
        for i in range(3):
            symbols.append(field[i][2 - i])
        if symbols == ['0', '0', '0']:
            return True, 'Нолики победили!!!'

        return False

    def ask_play():
        while True:
            x = input('Начать сначала?\n1 - Да\n2 - Нет\n:')
            flag = None

            if x == '1':
                flag = True
                return flag

            if x == '2':
                flag = False
                return flag

            if x != '1' != '2':
                print('Введите цифру 1 или 2!')

    great()
    num = 0
    while True:
        num += 1

        show()

        if num % 2 == 1:
            print('Ходит крестик')
        else:
            print('Ходит нолик')

        x, y = ask()

        if num % 2 == 1:
            field[x][y] = 'X'
        else:
            field[x][y] = '0'

        if num == 9:
            print('Ничья')
            break

        if check_win():
            print(f'Поздравляем!!!\n{check_win()[1]}')
            show()

            flag = ask_play()
            if flag is True:

                tic_tac_toe()
            else:
                break


tic_tac_toe()