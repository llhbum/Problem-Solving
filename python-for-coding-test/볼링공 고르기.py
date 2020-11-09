'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''

n, m = map(int, input().split())
nList = list(map(int,input().split()))

result = 0
for i in range(len(nList)):
    for j in range(i,len(nList)):
        if nList[i] != nList[j]:
            result += 1
print(result)
