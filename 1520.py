# 코드업 시간초과

a, b = map(int, input().split())

array = [[0]*(b+2) for _ in range(a+2)]
result = [[0]*(b+2) for _ in range(a+2)]

x, y, z = map(int, input().split())

for i in range(1, a+1):
    num_list = list(map(int, input().split()))
    for j in range(1, b+1):
        array[i][j] = num_list[j-1]
    num_list = []

k = int(input())

i_list = [-1, -1, -1, 0, 0, 1, 1, 1]
j_list = [-1, 0, 1, -1, 1, -1, 0, 1]


def cal(i, j):
    cnt = 0

    for k in range(8):
        if(array[i+i_list[k]][j+j_list[k]] == 1):
            cnt += 1

    return cnt


def list():
    for i in range(1, a+1):
        for j in range(1, b+1):
            array[i][j
                     ] = result[i][j]
            result[i][j] = 0

    return array, result


for _ in range(k):
    for i in range(1, a+1):
        for j in range(1, b+1):
            result_cnt = cal(i, j)
            if (array[i][j] == 1):
                if(1 <= result_cnt < 5):
                    result[i][j] = 1
                elif(result_cnt >= 5):
                    result[i][j] = 0
            elif(array[i][j] == 0):
                if(result_cnt == 2):
                    result[i][j] = 1
    list()

for i in range(1, a+1):
    for j in range(1, b+1):
        print(array[i][j], end=' ')
    print(' ')
