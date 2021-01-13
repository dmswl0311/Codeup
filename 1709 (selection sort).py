import sys
import time

start = time.time()

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 선택 정렬
for i in range(n):
    max = i
    for j in range(i+1, n):
        if(a[max] < a[j]):
            max = j
    a[i], a[max] = a[max], a[i]

for i in a:
    print(i, end=' ')

end = time.time()
print("time:", end-start)
