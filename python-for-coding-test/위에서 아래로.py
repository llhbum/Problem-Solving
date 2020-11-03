'''
3
15
27
12
'''

numList = []
n = int(input())
for i in range(n):
    numList.append(int(input()))
numList.sort(reverse=True)
print(numList)