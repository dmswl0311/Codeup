a, b = map(int, input().split())
result = bin(a | b)
print(int(result, 2))
