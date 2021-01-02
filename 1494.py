# 테케 오류 -> 배열의 크기를 정해야함

n, k = map(int, input().split())
d = [0]*n
result = [0]*n

for i in range(k):
    s, e, u = map(int, input().split())
    d[s-1] = d[s-1]+u
    d[e] = d[e]-u

start = 0
for i in range(n):
    result[i] = start+d[i]
    start = result[i]
    print(d[i], end=' ')
print(' ')

for i in range(n):
    print(result[i], end=' ')
