from collections import deque

gametime2 = 300
maze2 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', 'o', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', 'o', '#'],
    ['#', 'o', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', '#'],
    ['#', '#', '#', ' ', '#', '#', 'E', '#', '#', ' ', '#', '#', 'E', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', 'C', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', 'D', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

gametime = gametime2
maze = maze2

ROWS, COLS = len(maze), len(maze[0])

start = end = None
items = set()
for r in range(ROWS):
    for c in range(COLS):
        if maze[r][c] == 'S':
            start = (r, c)
        elif maze[r][c] == 'G':
            end = (r, c)
        elif maze[r][c] == 'o':
            items.add((r, c))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]


def is_accessible(maze, new_point):
    x, y = new_point
    return maze[x][y] != '#'


def bfs():
    global gametime
    visited = set()
    
    queue = deque([(start, frozenset(), 0, [])])
    
    while queue:
        (r, c), collected, steps, directions_seq = queue.popleft()

        if steps > gametime:
            continue

        if (r, c) == end and collected == items:
            return directions_seq

        for i, (dr, dc) in enumerate(directions):
            new_r, new_c = r + dr, c + dc
            new_pos = (new_r, new_c)

            if is_accessible(maze,new_pos) and (new_r, new_c, collected) not in visited:
                new_collected = collected | ({(new_r, new_c)} if maze[new_r][new_c] == 'o' else set())
                new_directions_seq = directions_seq + ['udlrw'[i]]
                queue.append(((new_r, new_c), new_collected, steps + 1, new_directions_seq))
                visited.add((new_r, new_c, new_collected))

    return None

directions_seq = bfs()
if directions_seq:
    print("Path:", ''.join(directions_seq))
else:
    print("No Path")