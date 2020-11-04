'''
INPUT
5
8 3 7 9 2
3
5 7 9
'''

n = int(input())
nList = list(map(int, input().split())) # 왜 set을 써야하나?
m = int(input())
mList = list(map(int, input().split()))

resultList = []

for i in range(m):
    if mList[i] in nList:
        resultList.append('yes')
    else:
        resultList.append('no')
# 출력
for result in resultList:
    print(result, end=' ')
