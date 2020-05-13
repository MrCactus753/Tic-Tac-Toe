# imports
from string import digits


# functions
def main_grid():
    global elements
    print('---------')
    print('|', ' '.join(elements[:3]), '|')
    print('|', ' '.join(elements[3:6]), '|')
    print('|', ' '.join(elements[6:]), '|')
    print('---------')


def coordinate_checker():
    global elements, last_move
    coordinates = {'1 3': elements[0],
                   '2 3': elements[1],
                   '3 3': elements[2],
                   '1 2': elements[3],
                   '2 2': elements[4],
                   '3 2': elements[5],
                   '1 1': elements[6],
                   '2 1': elements[7],
                   '3 1': elements[8]
                   }

    x = input('Enter the coordinates: ')
    if all(i for i in x.split() if i in digits):
        if all(int(i) in [1, 2, 3] for i in x.split()):
            if coordinates[x] == ' ':
                if last_move == 'O':
                    coordinates[x] = 'X'
                    elements = [i for i in coordinates.values()]
                    last_move = 'X'
                    return elements
                else:
                    coordinates[x] = 'O'
                    elements = [i for i in coordinates.values()]
                    last_move = 'O'
                    return elements

            else:
                print('This cell is occupied! Choose another one!')
                coordinate_checker()
        else:
            print("Coordinates should be from 1 to 3!")
            coordinate_checker()
    else:
        print('You should enter numbers!')
        coordinate_checker()


def game_conditions():
    global elements
    straights = [elements[:3],
                 elements[3:6],
                 elements[6:],
                 elements[0:9:3],
                 elements[1:9:3],
                 elements[2:9:3],
                 elements[0:9:4],
                 elements[2:7:2]
                 ]

    if ['X', 'X', 'X'] in straights:
        print('X wins')
        return 1
    elif ['O', 'O', 'O'] in straights:
        print('O wins')
        return 1
    elif elements.count(' ') > 0:
        return 0
    elif elements.count(' ') == 0:
        print('Draw')
        return 1


# main program
last_move = 'O'
elements = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
main_grid()

while True:
    coordinate_checker()
    main_grid()
    if game_conditions() > 0:
        break
