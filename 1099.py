# 시간초과 ㅂㄷㅂㄷ

array = [[0]*10 for _ in range(10)]

for i in range(10):
    flag = 0
    input_list = list(map(int, input().split()))
    for j in input_list:
        array[i][flag] = j
        flag += 1

i = 1
j = 1

while(i <= 9 or j <= 9):
    if (array[1][1] == 2):
        array[1][1] = 9
        break
    else:
        array[1][1] = 9
        if (array[i][j+1] == 0):
            j = j+1
            array[i][j] = 9

        elif (array[i][j+1] == 1):
            i = i+1
            if (array[i][j] == 0):
                array[i][j] = 9
            elif(array[i][j] == 1):
                break
            else:
                array[i][j] = 9
                break

for h in range(10):
    for w in range(10):
        print(array[h][w], end=' ')
    print('')
