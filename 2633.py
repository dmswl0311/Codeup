n, k = map(int, input().split())
array = sorted(list(map(int, input().split())))
result = 0
start = 0
end = n-1

while(start <= end):
    mid = (start+end)//2

    if k >= array[mid]:
        result = mid
        end = mid-1

    else:
        start = mid+1

print(result)
