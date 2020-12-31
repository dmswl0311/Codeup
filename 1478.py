n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
num = 1
flag=n

for k in range(n+m-1):
    for i in range(n):
        for j in range(m-1, -1, -1):
            if (i+j == flag):
                array[i][j] = num
                num += 1
                flag=(n-1)*2
            else:
                continue

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
