from collections import deque

def bfs(graph, start):
    visited = set()  # 用于跟踪已访问的节点
    queue = deque([start])  # 将起始节点加入队列

    while queue:
        vertex = queue.popleft()  # 从队列中取出一个节点
        if vertex not in visited:
            visited.add(vertex)  # 标记为已访问
            print(vertex)  # 访问节点，例如打印

            # 将所有邻接且未访问的节点加入队列
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 示例图
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # 从节点 A 开始遍历
