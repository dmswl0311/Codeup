import sys

input = sys.stdin.readline

n, k = map(int, input().split())
num = []

for i in range(1, n+1):
    if n % i == 0:
        num.append(i)
    else:
        continue

if len(num) < k:
    print(0)
else:
    print(num[k-1])
