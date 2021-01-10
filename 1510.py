n = int(input())

array = [[0]*n for _ in range(n)]

col = (n//2)
num = 1
array[0][col] = 1
row = 0-1
col = col+1

for k in range(2, (n*n)+1):
    if (col >= n):
        col = 0
    if (row < 0):
        row = n-1
    array[row][col] = k

    if (k % n == 0):
        row += 1
        col = col
    else:
        row -= 1
        col += 1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print(' ')
