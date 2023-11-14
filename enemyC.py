import os

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(maze):
    for row in maze:
        print(' '.join(row))
    print()

def find_enemy_C(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'C':
                return i, j
    return None

def is_accessible(maze, point):
    x, y = point
    return maze[x][y] != '#'

def move_enemy_C(maze, enemy_pos):
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  #l f r b
    ex, ey = enemy_pos

    for direction in directions:
        new_point = (ex + direction[0], ey + direction[1])
        if is_accessible(maze, new_point):
            maze[ex][ey], maze[new_point[0]][new_point[1]] = ' ', 'C'
            return new_point

    return enemy_pos

enemy_C_pos = find_enemy_C(maze)

while True:
    clear_screen()
    print_maze(maze)
    key = input("Enter command (c to move enemy C, q to quit): ").lower()
    
    if key == 'c':
        enemy_C_pos = move_enemy_C(maze, enemy_C_pos)
    elif key == 'q':
        break
