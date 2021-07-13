array = list(map(int, input().split()))


def bubble(array):
    for i in range(len(array)-1, 0, -1):
        swap = False
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if not swap:
            break


bubble(array)
print(array)
