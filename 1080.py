n = int(input())
sum = 0

for i in range(n+1):
    sum += i
    if sum >= n:
        print(i)
        break
