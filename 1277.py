import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

first = data[0]
second = 0
third = data[-1]

second = data[(n//2)]

print(first, second, third)
