import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

earn = a

for i in range(b):
    earn = earn+(earn*(data[i]/100))
    earn = earn

result = round(earn-a, 0)
print('%.0f' % result, end=' ')
print(' ')

if (result > 0):
    print('good')
elif (result == 0):
    print('same')
elif(result < 0):
    print('bad')
