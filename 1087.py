n = int(input())
i = 1
sum = 0

while(True):
    sum += i
    if sum >= n:
        break
    else:
        i += 1

print(sum)
