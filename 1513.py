n = int(input())
array = [[0]*n for _ in range(n)]

row = n-1
col = 0
num = 1

for k in range(n):
    if (k % 2 == 0):
        for _ in range(n-k):
            array[row][col] = num
            num += 1
            row -= 1
            col += 1
        row += 2
        col -= 1
    elif (k % 2 != 0):
        for i in range(n-k):
            array[row][col] = num
            num += 1
            row += 1
            col -= 1
        row -= 1
        col += 2

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print(' ')
