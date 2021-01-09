array = [[0]*11 for _ in range(11)]

for i in range(1, 10):
    num_list = list(map(int, input().split()))
    for j in range(1, 10):
        array[i][j] = num_list[j-1]
    num_list = 0

r, c = map(int, input().split())

i_list = [-1, -1, -1, 0, 0, 1, 1, 1]
j_list = [-1, 0, 1, -1, 1, -1, 0, 1]


def cal(i, j):
    cnt = 0
    for k in range(8):
        if (array[i+i_list[k]][j+j_list[k]] == 1):
            cnt += 1
    return cnt


if (array[r][c] != 1):
    print(cal(r, c))
elif (array[r][c] == 1):
    print(-1)
