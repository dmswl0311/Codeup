a, b = map(int, input().split())

sum = 0
sum2 = 0

for i in range(a, b+1):
    if i % 2 == 0:
        if i != b:
            print('-{0}+'.format(i), end='')
        else:
            print('-{0}'.format(i), end='')
        sum -= i
    else:
        print(i, end='')
        sum += i

print('={0}'.format(sum+sum2))
