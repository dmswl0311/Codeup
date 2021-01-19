from sys import stdin

result = [0]*101

for _ in range(7):
    result[int(stdin.readline())] += 1
cnt = 0
print(result)

for i in range(100, -1, -1):
    if(result[i] != 0):
        for j in range(result[i]):
            cnt += 1
            if cnt < 3:
                print(i)
            else:
                break
