'''
INPUT
5
2 3 1 2 2
'''

n = int(input())
nList = list(map(int,input().split()))
nList.sort()

result = 0
cnt = 0

for i in nList:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(result)
