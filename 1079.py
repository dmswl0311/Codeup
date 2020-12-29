list = list(map(str, input().split()))

for i in list:
    if i != 'q':
        print(i)
    elif i == 'q':
        print(i)
        break
