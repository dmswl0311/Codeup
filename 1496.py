n = int(input())
num_list = list(map(int, input().split()))
result = []

for i in range(n//2):
    if (num_list[2*i] >= num_list[(2*i)+1]):
        result.append(num_list[(2*i)+1])
    else:
        result.append(num_list[(2*i)])
    print(result[i], end=' ')
