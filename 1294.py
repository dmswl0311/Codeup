import sys
s = sys.stdin.readline()

for i in s:
    alpha = ord(i)

    if (97 <= alpha < 120):
        result = chr(alpha+3)
        print(result, end='')
    elif (alpha >= 120):
        result = chr(alpha-23)
        print(result, end='')
    elif (i == ' '):
        print(' ', end='')
