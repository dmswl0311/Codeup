import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a = sorted(b)


def search(a, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    if(a[mid] == target):
        return mid
    elif (a[mid] > target):
        return search(a, target, low, mid-1)
    else:
        return search(a, target, mid+1, high)


for i in b:
    target = i
    print(search(a, target, 0, n), end=' ')
