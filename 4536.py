import sys

input = sys.stdin.readline
l = []
cnt = [0]*1001
for i in range(10):
    l.append(int(input()))

for i in l:
    cnt[i] += 1

print(sum(l)//10)

for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i)
        break
