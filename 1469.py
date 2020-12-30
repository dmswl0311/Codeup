n = int(input())
array = [[0]*n for _ in range(n)]
k = 1

for i in range(n):
    if (i % 2 != 0):
        for j in range(n):
            array[i][j] = k
            k += 1
    else:
        for j in range(n-1, -1, -1):
            array[i][j] = k
            k += 1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print(' ')
