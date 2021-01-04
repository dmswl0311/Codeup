import sys

n, m = map(int, sys.stdin.readline().split())
array = [[0]*m for _ in range(n)]

flag = 1
num = 1

if n % 2 == 0:
    row = (n//2)-1
else:
    row = n//2
if m % 2 == 0:
    col = (m//2)
else:
    col = m//2

while(n != 0 and m != 0):
    if m % 2 == 0:
        for i in range(m):
            col += flag
            array[row][col] = num
            num += 1
        flag *= -1
        for i in range(n):
            row += flag
            array[row][col] = num
            num += 1
for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
