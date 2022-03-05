from collections import deque


def BFS(x, y):
    q.append([x, y])
    grid[y][x] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        t = q.popleft()
        tx = t[0]
        ty = t[1]
        # print("r", end=" ")
        for i3 in range(4):
            tempX = tx + dx[i3]
            tempY = ty + dy[i3]
            if 0 <= tempX < x and 0 <= tempY < y:
                if grid[tempY][tempX] == 1:
                    q.append([tempX, tempY])
                    grid[tempY][tempX] = 0


q = deque()
x = 10
y = 8
chunk = 0
grid = []
trueZone = 17
coordinates = [[0, 0], [1, 0], [1, 1], [4, 2], [4, 3], [4, 5], [2, 4], [3, 4], [7, 4], [8, 4], [9, 4], [7, 5], [8, 5],
               [9, 5], [7, 6], [8, 6], [9, 6]]
for i in range(y):
    grid.append([0] * x)
for i2 in range(trueZone):
    grid[coordinates[i2][1]][coordinates[i2][0]] = 1
print(grid)
for y1 in range(y):
    for x1 in range(x):
        if grid[y1][x1] == 1:
            BFS(x1, y1)
            print(grid)
            chunk += 1
print(grid)
print(chunk)