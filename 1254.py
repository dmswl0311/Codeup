start, end = map(str, input().split())

start = ord(start)
end = ord(end)

for i in range(end-start+1):
    result = start+i
    print(chr(result), end=' ')
