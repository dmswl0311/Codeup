import sys

n = int(sys.stdin.readline())
array = [0]*n

for i in range(n):
    array[i] = int(sys.stdin.readline())

for i in range(1, n):
    for j in range(i, 0, -1):
        if(array[i] < array[i-1]):
            array[i], array[i-1] = array[i-1], array[i]

for i in array:
    print(i)
