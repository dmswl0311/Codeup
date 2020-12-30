array = [[0]*10 for _ in range(10)]

for i in range(10):
    n = list(map(int, input().split()))
    for j in range(10):
        array[i][j] = n[j]
    n = []

i = 1
j = 1

while(i < 10 or j < 10):
    if (array[1][1] == 2):
        array[i][j] = 9
        break
    else:
        array[i][j] = 9
        if (array[i][j+1] == 1):
            if (array[i+1][j] == 1):
                break
            elif(array[i+1][j] == 0):
                i = i+1
            elif(array[i+1][j] == 2):
                i = i+1
                array[i][j] = 9
                break
        elif (array[i][j+1] == 0):
            j = j+1
        elif (array[i][j+1] == 2):
            j = j+1
            array[i][j] = 9
            break

for k in range(10):
    for m in range(10):
        print(array[k][m], end=' ')
    print(' ')
