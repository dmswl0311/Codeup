n = int(input())
x, y = map(int, input().split())
array = [[0]*n for _ in range(n)]

row = x-1
col = y-1

for i in range(n):
    num = i+1
    if (row-i >= 0):
        array[row-i][col] = num
    if (row+i < n):
        array[row+i][col] = num

for i in range(n):
    for j in range(1, y):
        array[i][col-j] = array[i][(col-j)+1]+1
    for j2 in range(1, (n-y)+1):
        array[i][col+j2] = array[i][(col+j2)-1]+1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print(' ')
