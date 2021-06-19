n = int(input())
n_list = list(map(int, input().split()))
result = 0
score = 1

for i in range(n):
    if (n_list[i] == 1):
        result += score
        score += 1
    else:
        score = 1

print(result)
