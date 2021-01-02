import sys

s = sys.stdin.readline()
result = int(s[0])

for i in range(len(s)-1):
    if (s[i] == '+'):
        result = result+int(s[i+1])
    elif(s[i] == '-'):
        result = result-int(s[i+1])
    elif(s[i] == '*'):
        result = result*int(s[i+1])
    elif(s[i] == '/'):
        result = result/int(s[i+1])
    else:
        continue


print('%d' % result)
