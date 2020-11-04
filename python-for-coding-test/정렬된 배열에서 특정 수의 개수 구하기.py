'''
INPUT
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''
from bisect import *
n, target = map(int,input().split())
nList = list(map(int,input().split()))

def bisec(nList, leftIndex, rightIndex):
    left_Index = bisect_left(nList,leftIndex)
    right_Index = bisect_right(nList, rightIndex)
    return right_Index - left_Index

result = bisec(nList,target,target)

if result == 0:
    print(-1)
else:
    print(result)


