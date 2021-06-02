import sys
input = sys.stdin.readline

n1 = int(input())
n2 = int(input())
l = []

for i in range(n1, n2+1):
    for j in range(1, i+1):
        if j != 1 and j != i and i % j == 0:
            break
        else:
            if j != 1 and j == i:
                l.append(i)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
