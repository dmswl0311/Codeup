month = int(input())

if month == 12 or month == 1 or month == 2:
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
elif month == 9 or month == 10 or month == 11:
    print("fall")

# 시간과, 메모리 더 걸리지만 사전형
month = int(input())
list = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring',
        6: 'summer', 7: 'summer', 8: 'summer', 9: 'fall', 10: 'fall', 11: 'fall'}
print(list[month])
