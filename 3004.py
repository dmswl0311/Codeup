import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
result = [0]*n

for i in range(n):
    num = 0
    for j in range(n):
        if a[i] > a[j]:
            num += 1
    result[i] = num

for i in result:
    print(i, end=' ')
