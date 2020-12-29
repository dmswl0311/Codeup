n = int(input())
k = list(map(int, input().split()))

start = 1
cnt = 0
for i in range(n):
    print(k[i])

while(n):
    for i in range(start, n):
        print(k[i], end=' ')
        print(k[cnt], end=' ')
    print('')
    start += 1
    cnt += 1
