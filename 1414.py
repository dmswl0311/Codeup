s = input().upper()
cnt = 0
cnt2 = 0
for i in range(len(s)):
    if s[i] == 'C':
        cnt += 1
        if i < len(s)-1 and s[i+1] == 'C':
            cnt2 += 1

print(cnt)
print(cnt2)
