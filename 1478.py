n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]

row = 0
col = m
num = 1
limit =

for k in range(limit):
    for i in range(0, k+1):
        array[row+i][col+(i-1)] = num
        num += 1
    row = row
    col = col-1

row = 0
col = 0
for k in range(limit, 0, -1):
    for i in range(0, k):
        array[row+i][col+i] = num
        num += 1
    row = row+1
    col = col

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
