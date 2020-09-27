'''

'''
x, y, w, h = map(int, input().split())
point_1 = abs(w - x)
point_2 = abs(h - y)
# point_3 = abs(x-point_1)
# point_4 = abs(y-point_2)
print(min(point_1, point_2, x, y))
