num = input()
cnt = 0
a = 5

for i in num:
    a = 4-cnt
    result = int(i)*10**a
    print('['+str(result)+']')
    cnt += 1
