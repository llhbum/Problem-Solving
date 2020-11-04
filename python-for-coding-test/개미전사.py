'''
INPUT
4
1 3 1 5

'''
# 오답 -> 홀짝으로 접근하면안됨
# n = int(input())
# nList = list(map(int,input().split()))
# answer = []
# d = [0] * 1000
# d[0] = nList[0]
# d[1] = nList[1]
# for i in range(2,n):
#     # print(i)
#     if i % 2 == 0:
#         nList[i] += d[i-2]
#     else:
#         nList[i] += d[i-2]
# print(max(nList[-1], nList[-2]))
# print(nList)

#정답
n = int(input())
nList = list(map(int,input().split()))
d = [0] * 100
d[0] = nList[0]
d[1] = max(d[0], nList[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + nList[i])

print(d[n-1])

