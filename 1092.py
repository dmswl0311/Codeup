import math

day1, day2, day3 = map(int, input().split())

print(math.gcd(math.gcd(day1, day2), day3))
