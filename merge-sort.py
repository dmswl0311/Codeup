def merge(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n//2
    g1 = merge(array[:mid])
    g2 = merge(array[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result


array = list(map(int, input().split()))
print(merge(array))
