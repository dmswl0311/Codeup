array = [[-1]*12 for _ in range(12)]
result = [[0]*12 for _ in range(12)]
for i in range(1, 11):
    num_list = list(map(int, input().split()))
    for j in range(1, 11):
        array[i][j] = num_list[j-1]
    num_list = 0


def cal(i, j, n):
    ori_i = i
    ori_j = j

    for k in range(ori_i-1, (ori_i-1)-n, -1):
        if (array[k][ori_j] == -1):
            break
        else:
            result[k][ori_j] = -2

    for k in range(ori_i+1, (ori_i+1)+n):
        if (array[k][ori_j] == -1):
            break
        else:
            result[k][ori_j] = -2

    for k in range(ori_j-1, (ori_j-1)-n, -1):
        if (array[ori_i][k] == -1):
            break
        else:
            result[ori_i][k] = -2

    for k in range(ori_j+1, (ori_j+1)+n):
        if (array[ori_i][k] == -1):
            break
        else:
            result[ori_i][k] = -2


for i in range(1, 11):
    for j in range(1, 11):
        if(array[i][j] >= 1):
            result[i][j] = -2
            cal(i, j, array[i][j])
        elif(array[i][j] == -1):
            result[i][j] = -1
        else:
            continue

n = int(input())

state = []

for i in range(n):
    r, c = list(map(int, input().split()))
    if (result[r][c] == 0):
        result[r][c] = i+1
        state.append('survive')
    else:
        state.append('dead')
        continue

for i in range(1, 11):
    for j in range(1, 11):
        print(result[i][j], end=' ')
    print(' ')

print('Character Information')
for i in range(n):
    print('player {0} {1}'.format(i+1, state[i]))
