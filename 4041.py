import sys
input = sys.stdin.readline

s = input().rstrip()
l = ""
result = 0
num = ""
flag = -1
for i in range(len(s)-1, -1, -1):
    l += s[i]

for i in range(len(l)):
    if i == 0 or flag != -1:
        if l[i] == '0':
            flag += 1
    if flag == -1 or l[i] != 0:
        num += l[i]
        result += int(l[i])

print(int(num))
print(result)
