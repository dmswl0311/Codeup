from collections import deque
from sys import stdin

m, n = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
zero = 0
one = 0
s = 0


def bfs(x, y):
    global s
    while(q):
        x, y, s = q.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]+1
                    s = graph[x][y]+1
                    q.append((nx, ny, s))
                elif graph[nx][ny] == -1:
                    continue


one_result = []
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # 퍼뜨리기
            q.append((i, j, s))
            one += 1
        elif graph[i][j] == 0:
            zero += 1
bfs(i, j)
flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
            break
if zero == (m*n) or flag == 1:
    print(-1)
elif one == (m*n) or s == 0:
    print(0)
else:
    print(s-1)
