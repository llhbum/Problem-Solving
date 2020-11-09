'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''

n = input()
sList = []
d = 0
for i in n:
    if i.isnumeric():
        d += int(i)
    else:
        sList.append(i)
sList.sort()
sList.append(d)
print(sList)