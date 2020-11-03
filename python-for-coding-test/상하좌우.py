'''
5
R R R U D D
'''

n = int(input())
dir = list(input().split())
print(dir)

x,y = 1, 1
for i in range(len(dir)):
    if dir[i] == 'L':
        temp = y - 1
        if 0 < temp <= n:
            y = temp

    elif dir[i] == 'R':
        temp = y + 1
        if 0 < temp <= n:
            y = temp

    elif dir[i] == 'U':
        temp = x - 1
        if 0 < temp <= n:
            x = temp

    elif dir[i] == 'D':
        temp = x + 1
        if 0 < temp <= n:
            x = temp
print(x,y)
