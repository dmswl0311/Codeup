import math

n = int(input())
i = 1
while(True):
    result = i**2
    if (result <= n):
        i += 1
    else:
        break

k = n-((i-1)**2)

result = math.sqrt((i-1)**2)

print("%d %.0f" % (k, result))
