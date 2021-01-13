import sys

n = int(sys.stdin.readline())
array = [0]*n

for i in range(n):
    array[i] = int(sys.stdin.readline())

for i in range(1, n):
    for j in range(i, 0, -1):
        if(array[j] < array[j-1]):
            array[j], array[j-1] = array[j-1], array[j]

for i in array:
    print(i)
