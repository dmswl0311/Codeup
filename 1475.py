import sys

n, m = map(int, sys.stdin.readline().split())
array = [[0]*m for _ in range(n)]

num = 1
flag = 1

for j in range(m-1, -1, -1):
    if (flag % 2 != 0):
        for i in range(n):
            array[i][j] = num
            num += 1
    else:
        for i in range(n-1, -1, -1):
            array[i][j] = num
            num += 1
    flag += 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
