import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
cnt = 0

for _ in range(n):
    name, score = map(str, input().split())
    l.append((name, int(score), cnt))
    cnt += 1

l.sort(key=lambda x: (x[1], -x[2]), reverse=True)

for i in range(m):
    print(l[i][0])
