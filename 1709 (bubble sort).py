import sys
import time

start = time.time()

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 버블 소트
for i in range(n-1, 0, -1):
    for j in range(i):
        if(a[j] < a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]

for i in a:
    print(i, end=' ')

end = time.time()
print("time:", end-start)
