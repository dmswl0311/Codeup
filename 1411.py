n = int(input())
a = []
sum = 0

for i in range(n-1):
    num = int(input())
    a.append(num)

for i in range(n+1):
    sum += i
for i in a:
    sum -= i
print(sum)
