import sys
import time
start = time.time()
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-i-1):
        if (array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
        else:
            continue

for i in array:
    print(i)

end = time.time()
print(end-start)
