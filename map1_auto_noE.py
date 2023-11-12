from collections import deque

# 定义迷宫布局
maze = [
    "###########",
    "#o   #   G#",
    "# ##   ## #",
    "# # o#o   #",
    "# # ### # #",
    "#S   o   o#",
    "###########"
]

# 迷宫的行数和列数
ROWS, COLS = len(maze), len(maze[0])

# 寻找起点、终点和物品的位置
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

# 有效移动的方向（左、右、上、下）
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 检查坐标是否在迷宫内部并且是可行走的路径
def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] != '#'

def bfs():
    # 队列中的元素为：(当前位置, 已收集的物品集, 步数, 移动方向序列)
    queue = deque([(start, frozenset(), 0, [])])
    visited = set()  # 用于记录已访问的状态

    while queue:
        (r, c), collected, steps, directions_seq = queue.popleft()

        # 如果步数超过限制，则继续下一个状态
        if steps > 50:
            continue

        # 检查是否到达目标且收集了所有物品
        if (r, c) == end and collected == items:
            return directions_seq

        for i, (dr, dc) in enumerate(directions):
            new_r, new_c = r + dr, c + dc

            if is_valid(new_r, new_c) and (new_r, new_c, collected) not in visited:
                new_collected = collected | ({(new_r, new_c)} if maze[new_r][new_c] == 'o' else set())
                new_directions_seq = directions_seq + ['lrud'[i]]  # 添加对应的移动方向
                queue.append(((new_r, new_c), new_collected, steps + 1, new_directions_seq))
                visited.add((new_r, new_c, new_collected))

    return None  # 如果没有找到路径，则返回 None

# 执行 BFS 并打印结果
directions_seq = bfs()
if directions_seq:
    print("移动序列:", ''.join(directions_seq))
else:
    print("没有找到路径")