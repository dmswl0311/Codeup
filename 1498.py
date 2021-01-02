n, g = map(int, input().split())
num_list = list(map(int, input().split()))

if (n % g == 0):
    for i in range(n//g):
        result = sorted(num_list[i*g:((i+1)*g)])
        print(result[0], end=' ')

else:
    for i in range((n//g)+1):
        if ((i+1)*g > n):
            result = sorted(num_list[i*g:])
        else:
            result = sorted(num_list[i*g:((i+1)*g)])
        print(result[0], end=' ')
