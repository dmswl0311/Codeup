target = int(input())
m_list = list(map(int, input().split()))
length = len(m_list)

m_list.sort()
left = 0
right = length-1

while left <= right:
    mid = (left+right)//2
    if m_list[mid] == target:
        print(mid+1)
        break
    elif m_list[mid] > target:
        right = mid-1
    else:
        left = mid+1

"""
target=25
m_list=30 94 27 92 21 37 25 47 25 53 98 19 32 32 7
"""
