# 처음 빼고는 방향 2개를 거칠 때마다 대입할 수 있는 숫자의 개수가 달라짐! -> 변수로 두자
# arrayp[i][j] 쓰면 안됨. 2차원 배열의 인덱스를 이동할 변수 2개 따로 만들어야 함 -> row, col
# 전체 반복횟수는 n번 -> 2개씩 출력하니까 (그림 그리면 이해 쉬움)

n = int(input('정사각형의 크기를 입력하세요: '))
array = [[0]*n for _ in range(n)]

row = 0
col = -1
num = 1
flag = 1

for count in range(n):
    for _ in range(n):
        col += flag
        array[row][col] = num
        num += 1
    n = n-1
    for _ in range(n):
        row += flag
        array[row][col] = num
        num += 1
    flag *= -1

print(array)
