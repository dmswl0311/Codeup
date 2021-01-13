import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n-1, 0, -1):
    swap = 0
    for j in range(i):
        if (array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            swap += 1
    cnt += 1
    if swap == 0:
        break

print(cnt-1)
# a
