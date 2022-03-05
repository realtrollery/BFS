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
