'''
2
홍길동 95
이순신 77
'''

nDict = {}
n = int(input())
for i in range(n):
    key, value = input().split()
    nDict[key] = int(value)

nDict = sorted(nDict.items())

print(nDict)
