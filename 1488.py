import sys

n, m = map(int, sys.stdin.readline().split())
array = [[0]*m for _ in range(n)]

flag = -1
num = 1
row = n-1
col = m
result_n = n
result_m = m

while(n != 0 and m != 0):
    for _ in range(m):
        col += flag
        array[row][col] = num
        num += 1
    n = n-1
    for _ in range(n):
        row += flag
        array[row][col] = num
        num += 1
    m = m-1
    flag *= -1

for i in range(result_n):
    for j in range(result_m):
        print(array[i][j], end=' ')
    print(' ')
