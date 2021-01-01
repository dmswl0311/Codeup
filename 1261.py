import sys

n_list = list(map(int, sys.stdin.readline().split()))
flag = 0

for i in n_list:
    if i % 5 == 0:
        flag = 1
        print(i)
        break
    else:
        continue

if flag == 0:
    print(0)
