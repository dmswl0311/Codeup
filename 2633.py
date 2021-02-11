n, k = map(int, input().split())
array = sorted(list(map(int, input().split())))
result = 0
start = 0
end = n-1
cnt = 0

while(start <= end):
    mid = (start+end)//2

    if k <= array[mid]:
        result = mid
        end = mid-1

    else:
        cnt += 1
        start = mid+1

if cnt == ((n-1)//2)+1:
    print(n+1)
else:
    print(result+1)
