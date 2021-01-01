a, b, c, n = map(int, input().split())
result = a

for _ in range(1, n):
    result = (result*b)+c
    result = result

print(result)
