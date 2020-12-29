a, b = map(int, input().split())
result = bin(a & b)  # 비트단위 연산
print(int(result, 2))  # 2진수->10진수로 바꾸기
