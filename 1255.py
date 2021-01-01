a, b = map(float, input().split())
i = 0.01
result = a
while(result <= b):
    print('%.2f' % result, end=' ')
    result += i
