import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)

for i in a:
    print(i, end=' ')
