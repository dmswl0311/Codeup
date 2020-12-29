h, b, c, s = map(int, input().split())
result = (h*b*c*s)

print(round(result/8/1024/1024, 1), 'MB')
