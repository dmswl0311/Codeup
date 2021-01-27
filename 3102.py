n = int(input())
s = []
result = []


def push(x):
    s.push(x)


def top():
    if len(s) == 0:
        result.append(-1)
    else:
        result.append(s[-1])


def pop():
    s.pop()


def size():
    result.append(len(s))


def empty():
    if len(s) == 0:
        result.append('true')
    else:
        result.append('false')


for i in range(n):
    a = input()
    if a[0] in push:
