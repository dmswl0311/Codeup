# 메모리 초과 - 긴 문자열을 한꺼번에 받기 때문에 일어나는 문제, 파이썬으로 불가? 어려움
# 단일 반복문, readline()으로 입력받아보자-> 단일 반복문으로 바꿔도 메모리 초과

import sys

n = int(sys.stdin.readline())
list_n = list(map(int, input().split()))
m = int(sys.stdin.readline())
list_m = list(map(int, input().split()))
result = [0]*m

# for i in range(m):
#     for j in range(n):
#         if (list_m[i] == list_n[j]):
#             result[i] = 1
#         else:
#             continue
#     print(result[i], end=' ')

for i in range(m):
    if list_m[i] in list_n:
        print('1', end=' ')
    else:
        print('0', end=' ')
