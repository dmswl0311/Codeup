import sys
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

end = n-1

while(end > 0):
    swap = 0
    for j in range(end):
        if (array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            swap = j
        end = swap

for i in array:
    print(i)
