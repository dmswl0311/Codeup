n = int(input())
list = list(map(int, input().split()))
result_list = [0]*23
flag = 0

for i in range(23):
    flag = 0
    for j in list:
        if j == (i+1):
            flag += 1
        else:
            continue
    result_list[i] = flag

for i in result_list:
    print(i, end=' ')
