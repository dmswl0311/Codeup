a, r, n = map(int, input().split())

if r == 0:
    print(0)
else:
    print(a*(r**n)//r)
