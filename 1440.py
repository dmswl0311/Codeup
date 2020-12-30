import sys

n = int(sys.stdin.readline())
list = list(map(int, input().split()))

for i in range(n):
    print('{0}:'.format(i+1), end=' ')
    num = list[i]
    if (i == 0):
        result_list = list[1:]
    elif (i == n-1):
        result_list = list[:-1]
    else:
        result_list = list[0:i]+list[i+1:]

    for j in result_list:
        if (num == j):
            print('=', end=' ')
        elif (num > j):
            print('>', end=' ')
        elif (num < j):
            print('<', end=' ')
    print(' ')
