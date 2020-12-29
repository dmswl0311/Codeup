# 문제 이해 안됨

array = [[0]*19 for _ in range(19)]

for i in range(19):
    for j in range(19):
        array[i][j] = map(int, input().split)

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
