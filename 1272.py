k, h = map(int, input().split())
k_result = 0
h_result = 0

if (k % 2 != 0):
    for i in range(1, (k//2)+2):
        k_result = i
else:
    for i in range(1, (k//2)+1):
        k_result = i*10

if (h % 2 != 0):
    for i in range(1, (h//2)+2):
        h_result = i
else:
    for i in range(1, (h//2)+1):
        h_result = i*10

print(k_result+h_result)
