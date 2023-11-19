from collections import deque

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'o', ' ', ' ', 'A', '#', 'B', ' ', ' ', 'G', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', 'o', '#', 'o', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', 'S', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'o', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

# 初始化变量
gametime = 50
ROWS, COLS = len(maze), len(maze[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
start = end = None
items = set()
enemies = {}  # 用于存储敌人的位置和类型

# 扫描迷宫以初始化起点、终点、物品和敌人位置
for r in range(ROWS):
    for c in range(COLS):
        if maze[r][c] == 'S':
            start = (r, c)
        elif maze[r][c] == 'G':
            end = (r, c)
        elif maze[r][c] == 'o':
            items.add((r, c))
        elif maze[r][c] in ['A', 'B', 'C', 'D', 'E']:
            enemies[(r, c)] = maze[r][c]

def is_accessible(maze, point, enemies):
    x, y = point
    return maze[x][y] != '#' and point not in enemies

def move_enemy_func(enemy_pos, directions):
    ex, ey = enemy_pos
    for direction in directions:
        new_point = (ex + direction[0], ey + direction[1])
        if is_accessible(maze, new_point,enemies):
            return new_point
    return enemy_pos

def enemy_A(enemy_pos, player_pos) :
    ex, ey = enemy_pos
    px, py = player_pos

    dx = ex - px
    dy = ey - py

    dy_move = (0, -1) if dy > 0 else (0, 1)
    dx_move = (-1, 0) if dx > 0 else (1, 0)

    if dx != 0 and is_accessible(maze, (ex + dx_move[0], ey + dx_move[1]),enemies):
        direction = [dx_move]
    elif dy != 0 and is_accessible(maze, (ex + dy_move[0], ey + dy_move[1]),enemies):
        direction = [dy_move]
    else:
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)] # down left up right

    return move_enemy_func(enemy_pos, direction)  

def enemy_B(enemy_pos, player_pos) :
    ex, ey = enemy_pos
    px, py = player_pos

    dx = ex - px
    dy = ey - py

    dy_move = (0, -1) if dy > 0 else (0, 1)
    dx_move = (-1, 0) if dx > 0 else (1, 0)

    if dy != 0 and is_accessible(maze, (ex + dy_move[0], ey + dy_move[1]),enemies):
        direction = [dy_move]
    elif dx != 0 and is_accessible(maze, (ex + dx_move[0], ey + dx_move[1]),enemies):
        direction = [dx_move]
    else:
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] # up left down right
    return move_enemy_func(enemy_pos, direction)  

def enemy_C(enemy_pos, player_pos):     # left forward right back
    orientation = enemy_list[enemy_pos]['orientation']
    if orientation == 'up':
        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)] # left forward right back
    elif orientation == 'down':
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    elif orientation == 'left':
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    elif orientation == 'right':
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    else:
        direction = [(0, 0)]
    return move_enemy_func(enemy_pos, direction)  

def enemy_D(enemy_pos, player_pos) :
    orientation = enemy_list[enemy_pos]['orientation']
    if orientation == 'up':
        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)] # right forward left back
    elif orientation == 'down':
        direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    elif orientation == 'left':
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    elif orientation == 'right':
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    else:
        direction = [(0, 0)]

    return move_enemy_func(enemy_pos, direction)  

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
                enemy_list[(i, j)] = {'type': value, 'orientation': 'up'}

# 更新敌人位置的函数
def update_enemies(enemies, player_pos):
    new_enemies = {}
    for pos, type in enemies.items():
        if type == 'A':
            new_pos = enemy_A(pos, player_pos)
        elif type == 'B':
            new_pos = enemy_B(pos, player_pos)
        elif type == 'C':
            new_pos = enemy_C(pos, player_pos)
        elif type == 'D':
            new_pos = enemy_D(pos, player_pos)
        elif type == 'E':
            new_pos = enemy_E(pos, player_pos)

        new_enemies[new_pos] = type
    return new_enemies

def bfs():
    global gametime
    visited = set()
    queue = deque([(start, frozenset(), 0, [], enemies)])
    
    while queue:
        (r, c), collected, steps, path, current_enemies = queue.popleft()

        if steps > gametime:
            continue

        if (r, c) == end and collected == items:
            return path

        for i, (dr, dc) in enumerate(directions):
            new_r, new_c = r + dr, c + dc
            new_point = (new_r, new_c)

            if is_accessible(maze, new_point, current_enemies) and (new_r, new_c, collected) not in visited:
                new_collected = collected | ({new_point} if maze[new_r][new_c] == 'o' else set())
                new_path = path + ['udlrw'[i]]
                new_enemies = update_enemies(current_enemies, (new_r, new_c))
                new_state = (new_point, new_collected, steps + 1, new_path, new_enemies)
                queue.append(new_state)
                visited.add((new_r, new_c, new_collected))

    return None

# 运行 BFS 寻路算法
path = bfs()
if path:
    print("Path:", ''.join(path))
else:
    print("No path")
