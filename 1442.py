import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n-1):
    least = i
    for j in range(i+1, n):
        if(array[least] > array[j]):
            least = j
    if (least != i):
        array[i], array[least] = array[least], array[i]

for i in array:
    print(i)
