import sys

s = sys.stdin.readline()

for i in s:
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')
