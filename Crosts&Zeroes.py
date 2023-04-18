import random

while True:

    line = 0  # coordinates of the line on the play-field
    column = 0  # coordinates of the column on the play-field
    figure = ''  # figure that uses player
    pc_figure = ''  # figure that uses computer
    game_stop = 0  # trigger to stop the game
    empty_block = 9  # counter of empty spots on the play-field

    # Create a play-field matrix

    field = [
        [' 0 ', ' 1 ', ' 2 ', ' 3 '],
        [' 1 ', "   ", "   ", "   "],
        [' 2 ', "   ", "   ", "   "],
        [' 3 ', "   ", "   ", "   "]
    ]


    # That function is to print the play-field

    def print_field():

        print("-" * 31)
        print("Игровое поле:")
        print('-' * 17)
        for i in field:
            print(f"|{'|'.join(i)}|")
            print('-' * 17)


    # This function is to input user's move coordinates

    def your_turn(block):
        while True:
            print("Ваш ход!")
            line = input('Строка от 1 до 3: ')
            column = input('Столбик от 1 до 3: ')
            if not line.isdigit() or not column.isdigit():  # check if input is digits
                print("Так ходить нельзя!")
            elif int(line) < 1 or int(line) > 3 or 1 > int(column) or int(
                    column) > 3:  # check if input is in range 0 to 3
                print("Так ходить нельзя!")
            elif field[int(line)][int(column)] == ' X ' or field[int(line)][int(column)] == ' O ':
                print('Эта клетка занята!')  # check if the spot on the play-field is not empty
            else:
                block -= 1
                return line, column, block


    # This function randomize coordinates of computer moves and return it to global "line", "column" and "empty_block"

    def pc_turn(block):
        while True:
            line = random.randint(1, 3)
            column = random.randint(1, 3)
            if field[line][column] != '   ':
                continue
            else:
                block -= 1
                print(f'{line}X{column}')
                return line, column, block


    # This function is to check all possible victory lines on the play-field

    def win_ckeck(winner, game_stop):
        if field[1][1] == field[1][2] == field[1][3] == winner or field[2][1] == field[2][2] == field[2][3] == winner or \
                field[3][1] == field[3][2] == field[3][3] == winner or field[1][1] == field[2][1] == field[3][
            1] == winner or \
                field[1][2] == field[2][2] == field[3][2] == winner or field[1][3] == field[2][3] == field[3][
            3] == winner or \
                field[1][1] == field[2][2] == field[3][3] == winner or field[1][3] == field[2][2] == field[3][
            1] == winner:
            if winner == figure:
                game_stop = 1
                print('Поздравляю! Вы победили!')
                return game_stop
            elif winner == pc_figure:
                game_stop = 1
                print("В этот раз победа за мной!")
                return game_stop


    # That function asks user if he wants to play one more time

    def end_of_game(answer):
        while True:
            if answer.isalpha():  # check if input is alpha
                if answer == "y":
                    return True
                elif answer == "n":
                    return False
                else:
                    print("Неправильный выбор!")
            else:
                print("Неправильный выбор!")
            answer = input('Надо выбрать "y" или "n": ')


    # Asking the player to choose a figure if it's "x" than computer gets "o"  and vice versa

    while True:
        print('======="Крестики Нолики"=======')
        figure = input('Чем хотите играть "x" или "o"? ')
        if figure != 'x' and figure != 'o':  # check if the choice is exactly "x" or "o"
            print("Такой знак недопустим!")
        elif figure == "x":
            pc_figure = ' O '
            figure = ' X '
            break
        else:
            pc_figure = ' X '
            figure = ' O '
            break

    print_field()

    while True:

        line, column, empty_block = your_turn(empty_block)

        field[int(line)][int(column)] = figure

        print_field()

        game_stop = win_ckeck(figure, game_stop)

        if game_stop == 1:
            break

        print(f"Я хожу так:")

        line, column, empty_block = pc_turn(empty_block)

        field[line][column] = pc_figure

        print_field()

        game_stop = win_ckeck(pc_figure, game_stop)

        if empty_block == 0:
            print("Ничья!")
            break
        elif game_stop == 1:
            break

    answer = input('Играем еще раз: "y" или "n"? ')         # Option to start a new game or to break the cicle

    if end_of_game(answer):
        continue
    else:
        print("Приятно было поиграть.")
        print()
        break

