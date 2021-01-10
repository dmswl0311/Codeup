import sys
n, m = map(int, sys.stdin.readline().split())
array = [[0]*m for _ in range(n)]

row = n
col = 0
num = n*m
flag = -1
limit_m = m
limit_n = n

while(limit_n != 0 and limit_m != 0):
    for _ in range(limit_n):
        row += flag
        array[row][col] = num
        num -= 1
    limit_m -= 1
    flag *= -1
    for _ in range(limit_m):
        col += flag
        array[row][col] = num
        num -= 1
    limit_n -= 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
