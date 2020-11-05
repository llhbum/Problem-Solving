'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int,input().split())
G = [ [INF] * (n+1) for _ in range(n+1) ]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            G[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

# x = 목적지
# k = 경유지
x, k = map(int, input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            G[a][b] = min(G[a][b], G[a][k] + G[k][b])
distance = G[1][k] + G[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)



'''
[
[0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
[1000000000, 0, 1, 1, 1, 1000000000], 
[1000000000, 1000000000, 0, 1000000000, 1, 1000000000], 
[1000000000, 1000000000, 1000000000, 0, 1, 1], 
[1000000000, 1000000000, 1000000000, 1000000000, 0, 1]
]
'''





