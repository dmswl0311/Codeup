import sys

n = int(sys.stdin.readline())
score = [0]*n
for i in range(n):
    math, info = map(int, sys.stdin.readline().split())
    score[i] = ((math, info, i+1))

score.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

for x in score:
    print(x[2], x[0], x[1], end=' ')
    print()
