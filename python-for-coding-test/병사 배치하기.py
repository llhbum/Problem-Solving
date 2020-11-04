'''
INPUT
7
15 11 4 8 5 2 4
'''

n = int(input())
nList = list(map(int,input().split()))
cnt = 0
dp = [1] * n
nList.reverse()

for i in range(1, n):
    for j in range(0, i):
        if nList[j] < nList[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
