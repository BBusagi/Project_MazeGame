# cus
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

player_point = [1, 1]  # Amn, init

def print_maze(maze, player_point):
    for m, row in enumerate(maze):
        for n, cell in enumerate(row):
            if [m, n] == player_point:
                print('S', end='')
            else:
                print(cell, end='') #point1
        print()


print_maze(maze, player_point)