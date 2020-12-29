# round() 말고 %.2f

w, h, b = map(float, input().split())
result = w*h*b
print('%.2f MB' % (result/8/1024/1024))
