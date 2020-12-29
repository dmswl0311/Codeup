n = int(input())
list = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(list[i], end=' ')
