n = int(input())
flag = 1

for i in range(n):
    for j in range(n):
        print(flag, end=' ')
        flag += 1
    print(' ')
