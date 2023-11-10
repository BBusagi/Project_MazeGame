import os
import msvcrt
import time

# cus
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'A', 'B', 'C', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D', 'E', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

player_point = [1, 1]  # Amn, init

collected = 0
new_point = [0,0]

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
    # test point
    global new_point
    global collected
    print("new_point", new_point)
    print("collected", collected)

def move_player(point, direction):
    m, n = point
    global new_point
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
    
    return event(point,new_point)

def event(point,new_point):

    element = maze[new_point[0]][new_point[1]]
    if element == '#':
        return point
    elif element == 'G':
        print("YOU WIN, CONGRATULATIONS!")
        while True:
            time.sleep(3)
    elif element == 'o':
        global collected
        collected += 1
        maze[new_point[0]][new_point[1]] = ' '
    elif element in ['A', 'B', 'C', 'D', 'E']:
        print("YOU LOSS, GAME OVER")
        while True:
            time.sleep(3)
    return new_point

print_maze(maze, player_point)

while True:
    key = msvcrt.getch().decode('utf-8').lower() #point2
    if key in ['w', 'a', 's', 'd', 'q']:
        player_point = move_player(player_point, key)
        clear_screen()
        print_maze(maze, player_point)


