n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m-(1-i), m-(2-i), -1):
        if(i+j == j):
            array[i][j] = i+1


for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
