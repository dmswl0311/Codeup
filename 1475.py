# 최대 1024 바이트?

n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
k = 1

for i in range(m-1, -1, -1):
    if (i % 2 == 0):
        for j in range(n):
            array[j][i] = k
            k += 1
    else:
        for j in range(n-1, -1, -1):
            array[j][i] = k
            k += 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
