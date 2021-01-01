s = input()
cnt = 0

for i in range(len(s)):
    if s[i] == 'l':
        if i < len(s)-3 and s[i+1] == 'o' and s[i+2] == 'v' and s[i+3] == 'e':
            cnt += 1
cnt = 0

# 최적 코드
for i in range(len(s)-4):
    if s[i:i+4] == 'love':
        cnt += 1
print(cnt)
