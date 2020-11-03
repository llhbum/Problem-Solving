'''
5 3
1 2 5 4 3
5 5 6 6 5
'''

n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))

aList.sort()
bList.sort(reverse=True)

for i in range(k):
    aList[i], bList[i] = bList[i], aList[i]
print(sum(aList))