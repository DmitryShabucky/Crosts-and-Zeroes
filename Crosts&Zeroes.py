import random

line = 0            # coordinates of the line on the play-field
column = 0          # coordinates of the column on the play-field
figure = ''         # figure that uses player
pc_figure = ''      # figure that uses computer
game_stop = 0       # trigger to stop the game
empty_block = 9     # counter of empty spots on the play-field

# Create a play-field matrix

field = [
    [' * ', ' 0 ', ' 1 ', ' 2 '],
    [' 0 ', "   ", "   ", "   "],
    [' 1 ', "   ", "   ", "   "],
    [' 2 ', "   ", "   ", "   "]
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

def your_turn():
    global empty_block
    global line
    global column
    while True:
        print("Ваш ход!")
        line = input('Строка от 0 до 2: ')
        column = input('Столбик от 0 до 2: ')
        if not line.isdigit() or not column.isdigit():                              # check if input is digits
            print("Так ходить нельзя!")
        elif int(line) < 0 or int(line) > 2 or 0 > int(column) or int(column) > 2:  # check if input is in range 0 to 2
            print("Так ходить нельзя!")
        elif field[int(line) + 1][int(column) + 1] == ' x ' or field[int(line) + 1][int(column) + 1] == ' o ':
            print('Эта клетка занята!')                           # check if the spot on the play-field is not empty
        else:
            empty_block -= 1
            return line, column

# This function randomize coordinates of computer moves and return it to global "line", "column" and "empty_block"

def pc_turn():
    while True:
        global line
        global column
        global empty_block
        line = random.randint(0, 2)
        column = random.randint(0, 2)
        if field[line + 1][column + 1] != '   ':
            continue
        else:
            empty_block -= 1
            print(f'{line}X{column}')
            return line, column

# This function is to check all possible victory lines on the play-field

def win_ckeck(winner):
    global game_stop
    if field[1][1] == field[1][2] == field[1][3] == winner or field[2][1] == field[2][2] == field[2][3] == winner or \
            field[3][1] == field[3][2] == field[3][3] == winner or field[1][1] == field[2][1] == field[3][
        1] == winner or \
            field[1][2] == field[2][2] == field[3][2] == winner or field[1][3] == field[2][3] == field[3][
        3] == winner or \
            field[1][1] == field[2][2] == field[3][3] == winner or field[1][3] == field[2][2] == field[3][1] == winner:
        if winner == figure:
            game_stop = 1
            print('Поздравляю! Вы победили!')
        elif winner == pc_figure:
            game_stop = 1
            print("В этот раз победа за мной!")


# Asking the player to choose a figure if it's "x" than computer gets "o"  and vice versa
while True:
    print('======="Крестики Нолики"=======')
    figure = input('Чем хотите играть "x" или "o"? ')
    if figure != 'x' and figure != 'o':                 # check if the choice is exactly "x" or "o"
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

    your_turn()

    field[int(line) + 1][int(column) + 1] = figure

    print_field()

    win_ckeck(figure)

    if game_stop == 1:
        break

    print(f"Я хожу так:")

    pc_turn()

    field[line + 1][column + 1] = pc_figure

    print_field()

    win_ckeck(pc_figure)

    if empty_block == 0:
        print("Ничья!")
        break
    elif game_stop == 1:
        break
