import sys
array = [[0]*100 for i in range(100)]
sum = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = 1
            if (array[i][j] == 1):
                array[i][j] = 2

for i in range(100):
    for j in range(100):
        if (array[i][j] == 2 or array[i][j] == 1):
            sum += 1
        else:
            continue

print(sum)
