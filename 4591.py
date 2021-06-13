num_list = []

for _ in range(9):
    num_list.append(int(input()))


print(max(num_list))

for i in range(len(num_list)):
    if num_list[i] == max(num_list):
        print(i+1)
        break
