m, n, x, y = map(int, input().split())

array = [[0]*m for _ in range(n)]

for i in range(n):
    num_list = list(map(int, input().split()))
    for j in range(m):
        array[i][j] = num_list[j]
    num_list = 0

flag = 0
sum = 0

for i in range(n-y+1):
    for j in range(m-x+1):
        for k in range(y):
            for l in range(x):
                sum += array[i+k][j+l]
        if (sum > flag):
            flag = sum
        sum = 0

print(flag)
