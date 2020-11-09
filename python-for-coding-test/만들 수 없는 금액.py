'''
INPUT
5
3 2 1 1 9

'''

n = int(input())
nList = list(map(int, input().split()))

nList.sort()

'''
11239
'''
target = 1
for x in nList:
    if target < x:
        break
    target += x
print(target)