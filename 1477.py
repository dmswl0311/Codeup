n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
num = 1

for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if (i+j == k):
                array[i][j] = num
                num += 1
            else:
                continue

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
