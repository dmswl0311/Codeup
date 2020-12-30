n, c = map(int, input().split())

height = list(map(int, input().split()))
num = 0
height_sort = sorted(height)

for i in height_sort:
    print(i, end=' ')
    num += 1
    if (num % c == 0):
        print(' ')
