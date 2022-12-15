import random
turns = 0
print("Добро пожаловать в игру Морской Бой!")
Rows = int(input("Введите количество строк для поля, которое Вам нужно: "))
Columns = int(input("Введите количество столбцов для поля, которое Вам нужно: "))
def create_grid(Rows, Columns):
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

grid = create_grid(Rows,Columns)

def display_grid(grid, Columns):
    column_names = 'АБВГДЕЁЖЗИКЛМНОПРСТУФXЦЧШЩЭЮЯabcdefghijklmnopqrstuvwxyz'[:Columns]
    print('    | ' + ' | '.join(column_names) + ' |')
    for number, row in enumerate(grid):
        if number + 1 <= 9:
            print(number + 1, '  | ' + ' | '.join(row) + ' |')
        elif number + 1 >= 9:
            print(number + 1, ' | ' + ' | '.join(row) + ' |')

grid = create_grid(Rows, Columns)
display_grid(grid, Columns)
def random_row1(grid):
    return random.randint(1,len(grid))
def random_col1(grid):
    return random.randint(1,len(grid[0]))
def random_row2(grid):
    return random.randint(2,len(grid))
def random_col2(grid):
    return random.randint(2,len(grid[0]))
def update_gridHit(grid, GuessRow1, GuessColumn1):
    grid[GuessRow1-1][GuessColumn1-1] = 'O'
def update_gridMiss(grid, GuessRow1, GuessColumn1):
    grid[GuessRow1-1][GuessColumn1-1] = 'X'
# if Rows < 5 and Columns < 5:
ShipRow1 = random_row1(grid)
ShipColumn1 = random_col1(grid)
print(f'Координаты коробля #1: {ShipRow1},{ShipColumn1}')
# elif Rows >= 5 or Columns >= 5:
#     ShipRow1 = random_row1(grid)
#     ShipColumn1 = random_col1(grid)
#     ShipRow2 = random_row2(grid)
#     ShipColumn2 = random_col2(grid)
#     print(f'Координаты коробля #1: {ShipRow1},{ShipColumn1} \nКоординаты коробля #2: {ShipRow2},{ShipColumn2}')

while (turns != 5):
    GuessRow1 = int(input("В какую строку будем стрелять? \n"))
    GuessColumn1 = int(input("В какой столбик делать залп? \n"))

    if (GuessRow1 == ShipRow1) and (GuessColumn1 == ShipColumn1):
        turns += 1
        update_gridHit(grid, GuessRow1, GuessColumn1)
        display_grid(grid, Columns)
        print("Вы уничтожили корабль! Поздравляю!")
        break

    else:
        if (GuessRow1 < 1 or GuessRow1 > Rows) or (GuessColumn1 < 1 or GuessColumn1 > Columns):
            print("Вы указали невернные координаты.")

        elif (grid[GuessRow1-1][GuessColumn1-1] == "X"):
            print("Вы уже стреляли в данную точку.")

        else:
            turns += 1
            print("Вы не попали. МИМО!")
            update_gridMiss(grid, GuessRow1, GuessColumn1)
            display_grid(grid, Columns)

    if (turns >= 5):
        print("Закончились попытки \n GAME OVER!" )

