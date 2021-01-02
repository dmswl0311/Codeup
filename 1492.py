import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
result = [0]*n
start = 0
for i in range(n):
    result[i] = start+num[i]
    start = result[i]
    print(result[i], end=' ')
