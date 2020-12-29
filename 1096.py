# 띄어쓰기 ㅂㄷㅂㄷ
# 2차원 배열 초기화방법 컴프리헨션 사용!

n = int(input())
array = [[0]*19 for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    array[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(array[i][j], end=' ')
    print('')
