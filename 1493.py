# 테스트 케이스 오류

import sys

n, m = map(int, sys.stdin.readline().split())
array = [[0]*m for _ in range(n)]

for i in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        array[i][j] = num_list[j]
    num_list = []

start = 0

for i in range(n):
    for j in range(m):
        array[i][j] = start+array[i][j]
        start = array[i][j]
    start = 0

if (n > 1):
    for j in range(m):
        for i in range(1, n):
            array[i][j] = array[i-1][j]+array[i][j]

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print(' ')
