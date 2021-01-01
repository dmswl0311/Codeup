n = int(input())
i = 1
while(True):
    if (n//(10**i) == 0):
        print(i)
        break
    else:
        i += 1
        continue
