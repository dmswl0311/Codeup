a, b = map(int, input().split())

for i in range(a+1, 1, -1):
    if (a % i == 0) and (b % i == 0):
        print(i)
        break

for i in range(b, (a*b)+1):
    if (i % a == 0) and (i % b == 0):
        print(i)
        break
