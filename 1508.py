import sys
n = int(sys.stdin.readline())
array = [[0]*n for _ in range(n)]

for t in range(n):
    k = int(sys.stdin.readline())
    array[t][0] = k
    for j in range(1, t+1):
        array[t][j] = array[t][j-1]-array[t-1][j-1]

for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            print(array[i][j], end=' ')
    print(' ')
