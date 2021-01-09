array = [[0]*25 for _ in range(25)]
result = [[0]*25 for _ in range(25)]

for i in range(25):
    num_list = list(map(int, input().split()))
    for j in range(25):
        array[i][j] = num_list[j]
    num_list = []


def life(i, j):
    zero_life = 0

    for k in range(-1, 2, 1):
        for col in range(j-1, j+2, 1):
            if(array[i+k][col] == 1):
                if(i+k == i and col == j):
                    continue
                else:
                    zero_life += 1
            else:
                continue

    return zero_life


for i in range(1, 24):
    for j in range(1, 24):
        cnt = life(i, j)
        if(array[i][j] == 0):
            if(cnt == 3):
                result[i][j] = 1
            else:
                result[i][j] = 0
        elif(array[i][j] == 1):
            if(4 <= cnt or cnt <= 1):
                result[i][j] = 0
            elif(cnt == 2 or cnt == 3):
                result[i][j] = 1
            else:
                result[i][j] = 0


for i in range(25):
    for j in range(25):
        print(result[i][j], end=' ')
    print('')
