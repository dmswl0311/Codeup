import sys

array = [[0]*10 for _ in range(10)]

for i in range(10):
    num_list = list(map(int, sys.stdin.readline().split()))
    for j in range(10):
        array[i][j] = num_list[j]
    num_list = []

horse_list = list(map(int, sys.stdin.readline().split()))

for s in range(10):
    flag = 0
    if (horse_list[s] != 0):
        for i in range(9, -1, -1):
            if (array[i][s] > 0):
                flag = 1
                print("{0} crash".format(s+1))
                break
            elif (array[i][s] < 0):
                flag = 1
                print("{0} fall".format(s+1))
                break
            elif (array[i][s] == 0):
                continue
        if flag == 0:
            print("{0} safe".format(s+1))
    else:
        continue
