import os
import msvcrt
import time

# cus
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', 'C', ' ', ' ', 'C', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

player_point = [1, 1]  # Amn, init
gametime = 50

collected = sum(row.count('o') for row in maze)
score = 0
result = []
new_point = [0,0]

def clear_screen():                                                                                      #point3
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(maze, player_point):
    global gametime
    print("time: ", gametime)
    for m, row in enumerate(maze):
        for n, cell in enumerate(row):
            if [m, n] == player_point:
                print('S', end='')
            else:
                print(cell, end='')                                                                     #point1
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
    global collected
    global gametime
    global score
    global result
    element = maze[new_point[0]][new_point[1]]
    if element == '#':
        return point
    elif element == 'G':
        if collected == 0:
            score = gametime
            print("YOU WIN, CONGRATULATIONS!")
            print("Score:", score)
            output = ''.join(result)
            print("Output:", output)
            while True:
                time.sleep(3)
    elif element == 'o':
        collected -= 1
        maze[new_point[0]][new_point[1]] = ' '
    elif element in ['A', 'B', 'C', 'D', 'E']:
        print("YOU LOSS, GAME OVER")
        while True:
            time.sleep(3)
    return new_point


# Enemy system

def is_accessible(maze, new_point):
    x, y = new_point
    return maze[x][y] == ' '
    #return maze[x][y] in [' ', 'G']    #point4

def move_enemy_func(enemy_pos, player_pos, directions):
    ex, ey = enemy_pos
    for direction in directions:
        new_point = (ex + direction[0], ey + direction[1])
        if is_accessible(maze, new_point):
            return new_point
    return enemy_pos

def enemy_A(enemy_pos, player_pos) :
    return move_enemy_func(enemy_pos, player_pos, [(1, 0), (0, -1), (-1, 0), (0, 1)])  # d l u r

def enemy_B(enemy_pos, player_pos) :
    return move_enemy_func(enemy_pos, player_pos, [(-1, 0), (0, -1), (1, 0), (0, 1)])  # u l d r

def enemy_C(enemy_pos, player_pos):
    return move_enemy_func(enemy_pos, player_pos, [(0, -1), (-1, 0), (0, 1), (1, 0)])  # l f r b

def enemy_D(enemy_pos, player_pos) :
    return move_enemy_func(enemy_pos, player_pos, [(0, 1), (-1, 0), (0, -1), (1, 0)])  # r f l b

enemy_E_state = 'C'
def enemy_E(enemy_pos, player_pos) :
    global enemy_E_state
    if enemy_E_state == 'C':
        new_pos = enemy_C(enemy_pos, player_pos)
        enemy_E_state = 'D'
    else:
        new_pos = enemy_D(enemy_pos, player_pos)
        enemy_E_state = 'C'
    return new_pos

enemy_behaviors = {
    'A': enemy_A,
    'B': enemy_B,
    'C': enemy_C,
    'D': enemy_D,
    'E': enemy_E
}

enemy_list = {}
def initialize_enemy_list():
    global enemy_list
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value in ['A', 'B', 'C', 'D', 'E']:
                enemy_list[(i, j)] = value

def move_enemy():
    global new_point, enemy_list
    current_positions = list(enemy_list.keys())

    for pos in current_positions:
        if pos not in enemy_list:
            continue

        enemy_type = enemy_list[pos]
        move_enemy_instance = enemy_behaviors[enemy_type]
        new_pos = move_enemy_instance(pos, new_point)

        if new_pos != pos:
            maze[pos[0]][pos[1]], maze[new_pos[0]][new_pos[1]] = ' ', maze[pos[0]][pos[1]]
            enemy_list[new_pos] = enemy_list.pop(pos)


initialize_enemy_list()
print_maze(maze, player_point)

while True:
    key = msvcrt.getch().decode('utf-8').lower()                                                            #point2
    result.append(key)
    if gametime == 0:
        print("YOU LOSS, GAME OVER")
        while True:
            time.sleep(3)
    if key in ['w', 'a', 's', 'd', 'q']:
        player_point = move_player(player_point, key)
        if maze[new_point[0]][new_point[1]] != '#':
            gametime -= 1
            move_enemy()
        clear_screen()
        print_maze(maze, player_point)
        
        # test point
        print(enemy_list)