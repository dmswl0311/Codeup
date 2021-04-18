from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 1

q = deque()
result_cnt = []


def bfs(x, y, result):
    cnt = 0
    q.append((x, y))
    graph[x][y] = result
    cnt += 1
    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = result
                cnt += 1
                q.append((nx, ny))
    result_cnt.append(cnt)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result += 1
            bfs(i, j, result)
print(result-1)
result_cnt.sort()

for i in result_cnt:
    print(i)
