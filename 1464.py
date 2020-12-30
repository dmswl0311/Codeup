n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
k = 1

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        array[i][j] = k
        k += 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
