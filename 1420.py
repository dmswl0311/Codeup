# 모르겠음..

n = int(input())
dic = dict()
for i in range(n):
    name, score = map(str, input().split())
    dic[name] = int(score)

print(dic)

third = sorted(dic.values())[2]
print(third)
for key, value in dic.items():
    if (value == third):
        print(key)
