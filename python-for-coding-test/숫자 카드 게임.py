'''
N은 행의 개수
M은 열의 개수

N*M

'''

"""
INPUT
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""

n, m = map(int, input().split())
tList = []
for _ in range(n):
    tList.append(list(map(int, input().split())))
    
minList = []
for i in tList:
    minList.append(min(i))
print(max(minList))