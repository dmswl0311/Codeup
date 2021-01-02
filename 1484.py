n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]
row = 0
col = -1
trans = 1  # 행열의 증가, 감소
cnt = 1
limit = 0

for count in range(1, n*m):
    for i in range(m-limit):
        col += trans
        array[row][col] = cnt
        cnt += 1
    for i in range(n-limit-1):
        row += trans
        array[row][col] = cnt
        cnt += 1
    limit += 1
    trans *= -1

print(array)
