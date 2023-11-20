# cus

gametime_test = 50
maze_test = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', 'A', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', 'o', 'o', ' ', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]

gametime1 = 50
maze1 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'o', ' ', ' ', 'A', '#', 'B', ' ', ' ', 'G', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', 'o', '#', 'o', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'o', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

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

gametime3 = 700
maze3 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'C', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', 'C', ' ', ' ', ' ', 'o', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', 'o', '#', '#', 'o', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', 'o', '#', '#', '#', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', 'o', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', ' ', 'o', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', 'o', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', 'D', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'D', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', 'A', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', 'o', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', 'o', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'E', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', '#', '#', 'G', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', 'o', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'C', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

player_point = [5, 1]  # Amn, init