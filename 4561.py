num_list = []
sum = 0
de = 100

for _ in range(7):
    num_list.append(int(input()))

for i in num_list:
    if i % 2 != 0:
        sum += i
        de = min(i, de)

if sum == 0:
    print(-1)
else:
    print(sum)
    print(de)
