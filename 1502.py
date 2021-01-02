n = int(input())
array = [[0]*n for _ in range(n)]
flag = 1

for j in range(n):
    for i in range(n):
        array[i][j] = flag
        flag += 1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print(' ')
