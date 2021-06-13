m = int(input())
n = int(input())

i = 1
result = []
while(True):
    if i*i > n:
        break
    if m <= i*i and i*i <= n:
        result.append(i*i)
    i += 1

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
