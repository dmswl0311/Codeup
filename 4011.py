import sys
input = sys.stdin.readline

s = input().rstrip()

year = s[:2]
month = s[2:4]
day = s[4:6]
g = s[7]
flag = -1

"""
flag가 0이면 2000년 이전 출생
1이면 2000년 이후 출생
"""

if (g == "1") or (g == "3"):
    if g == "1":
        flag = 0
    else:
        flag = 1
    gender = "M"

elif (g == "2") or (g == "4"):
    if g == "2":
        flag = 0
    else:
        flag = 1
    gender = "F"

if flag == 0:
    print("19"+year+"/"+month+"/"+day+" "+gender)
elif flag == 1:
    print("20"+year+"/"+month+"/"+day+" "+gender)
