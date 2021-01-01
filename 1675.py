import sys

s = sys.stdin.readline()

for i in s:
    alpha = ord(i)
    if (i == ' '):
        print(i, end='')
    elif (100 <= alpha <= 122):
        result = chr(alpha-3)
        print(result, end='')
    elif(97 <= alpha < 100):
        result = chr(alpha+23)
        print(result, end='')
