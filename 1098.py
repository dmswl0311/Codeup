h, w = map(int, input().split())
n = int(input())
array = [[0]*w for _ in range(h)]
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            array[x-1][y-1+j] = 1
    else:
        for k in range(l):
            array[x+k-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(array[i][j], end=' ')
    print('')
