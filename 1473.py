n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
k = 1
flag = 1

for i in range(n-1, -1, -1):
    if (flag % 2 != 0):
        for j in range(m):
            array[i][j] = k
            k += 1
        flag += 1
    else:
        for j in range(m-1, -1, -1):
            array[i][j] = k
            k += 1
        flag += 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
