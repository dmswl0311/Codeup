s = input()

for i in s:
    password1 = chr(ord(i)+2)
    print(password1, end='')
print(' ')

for i in s:
    password2 = chr((ord(i)*7) % 80+48)
    print(password2, end='')
