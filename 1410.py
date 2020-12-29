string = input()
sum = 0
sum2 = 0
for i in string:
    if (i == '('):
        sum += 1
    elif (i == ')'):
        sum2 += 1

print(sum, sum2)
