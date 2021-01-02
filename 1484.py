n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
result_n = n
result_m = m
row = 0
col = -1
flag = 1
num = 1

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
