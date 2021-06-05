import sys
input = sys.stdin.readline

a, b, c, d, e, f, g = map(int, input().split())

num = [a, b, c, d, e, f, g]
result = 0
cnt = 0

for i in range(7):
    if num[i] % 2 == 0:
        cnt += 1
        continue
    else:
        result += num[i]

if cnt == 7:
    print(-1)
else:
    print(result)
