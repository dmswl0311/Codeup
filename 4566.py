n = int(input())
m = int(input())

result = []
if n == 1:
    n = 2
for i in range(n, m+1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break

    if flag == 0:
        result.append(i)

if len(result) > 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)
