import sys

n = int(sys.stdin.readline())
dic = dict()

for i in range(n):
    name, score = map(str, sys.stdin.readline().split())
    dic[int(score)] = name

dic2 = sorted(dic.keys(), reverse=True)

print(dic.get(dic2[2]))
