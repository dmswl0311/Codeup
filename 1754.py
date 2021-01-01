import sys

a, b = map(int, sys.stdin.readline().split())

if a < b:
    print(a, b)
else:
    print(b, a)
