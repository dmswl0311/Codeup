n = int(input())
list = list(map(int, input().split()))

for i in range(1, len(list)+1):
    print(list[-i], end=' ')
