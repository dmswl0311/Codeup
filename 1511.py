n = int(input())
array = [[0]*n for _ in range(n)]
num = 0
len = 0
wid = 0
for i in range(n):
    for j in range(n):
        num += 1
        array[i][j] = num
        if i == 0 or i == (n-1):
            wid += num
        else:
            if (j == 0 or j == (n-1)):
                len += num
            else:
                continue

print(len+wid)
