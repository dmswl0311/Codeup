a, b = map(int, input().split())

for i in range(b-a+1):
    if (a+i) % 2 != 0:
        print(a+i, end=' ')
