from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 1

print(graph)

q = deque()


def bfs(x, y, result):
    q.append((x, y))
    graph[x][y] = result
    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                print("result= ", result, nx, ny)
                graph[nx][ny] = result
                q.append((nx, ny))


for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs(i, j, result)
            result += 1

print(graph)
