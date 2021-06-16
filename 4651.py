result = []

for _ in range(3):
    num_list = list(map(int, input().split()))
    cnt_zero = 0
    cnt_one = 0
    for i in num_list:
        if i == 0:
            cnt_zero += 1
        elif i == 1:
            cnt_one += 1
    if cnt_zero == 1 and cnt_one == 3:
        result.append("A")
    elif cnt_zero == 2 and cnt_one == 2:
        result.append("B")
    elif cnt_zero == 3 and cnt_one == 1:
        result.append("C")
    elif cnt_zero == 4:
        result.append("D")
    elif cnt_one == 4:
        result.append("E")

for i in result:
    print(i)
