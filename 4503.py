import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = 1

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(graph, visited, start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(graph, visited, i)


dfs(graph, visited, 1)
print(cnt-1)
