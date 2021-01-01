import sys

day1, day2, day3 = map(int, sys.stdin.readline().split())

result = 1

while(result % day1 != 0) and (result % day2 != 0) and (result % day3 != 0):
    result += 1

print(result)
