import sys

n = int(sys.stdin.readline())
array = [[0]*n for _ in range(n)]
num = 1
row = -1
col = 0
flag = 1
result_n = n
for i in range(n):
    for _ in range(n):
        row += flag
        array[row][col] = num
        num += 1
    n = n-1
    for _ in range(n):
        col += flag
        array[row][col] = num
        num += 1
    flag *= -1

for i in range(result_n):
    for j in range(result_n):
        print(array[i][j], end=' ')
    print(' ')
