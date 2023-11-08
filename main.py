import os
import msvcrt
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

def clear_screen(): #point3
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(maze, player_point):
    for m, row in enumerate(maze):
        for n, cell in enumerate(row):
            if [m, n] == player_point:
                print('S', end='')
            else:
                print(cell, end='') #point1
        print()

def move_player(point, direction):
    m, n = point
    new_point = [m, n]
    if direction == 'w':
        new_point[0] -= 1
    elif direction == 's':
        new_point[0] += 1
    elif direction == 'a':
        new_point[1] -= 1
    elif direction == 'd':
        new_point[1] += 1
    elif direction == 'q':
        return point
    return new_point

print_maze(maze, player_point)

while True:
    key = msvcrt.getch().decode('utf-8').lower() #point2
    if key in ['w', 'a', 's', 'd', 'q']:
        player_point = move_player(player_point, key)
        clear_screen()
        print_maze(maze, player_point)