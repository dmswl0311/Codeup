import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    name, score1, score2, score3 = map(str, input().split())
    l.append((name, int(score1), int(score2), int(score3)))

l.sort(key=lambda x: x[1], reverse=True)
result_name = l[0][0]

l.sort(key=lambda x: (x[2], x[1]), reverse=True)
for i in range(n):
    if l[i][0] == result_name:
        result_score2 = i+1
        break

l.sort(key=lambda x: (x[3], x[1]), reverse=True)
for i in range(n):
    if l[i][0] == result_name:
        result_score3 = i+1
        break

print("{0} {1} {2}".format(result_name, result_score2, result_score3))
