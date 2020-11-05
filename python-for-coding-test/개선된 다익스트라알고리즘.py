"""
INPUT
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""


import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
G = [[] for _ in range(n + 1)]
distanse = [INF] * (n + 1)

# 간선정보
for _ in range(m):
    a, b ,c = map(int, input().split())
    G[a].append((b,c))
print(G)
'''
[
[],
 [(2, 2), (3, 5), (4, 1)], 
 [(3, 3), (4, 2)], 
 [(2, 3), (6, 5)], 
 [(3, 3), (5, 1)], 
 [(3, 1), (6, 2)], 
 []
 ]
'''
def dijkstra(start):
    h = []
    heapq.heappush(h,(0,start))
    distanse[start] = 0
    while h:
        dist, node  = heapq.heappop(h)
        if distanse[node] < dist:
            continue
        for i in G[node]:
            cost = dist + i[1]
            if cost < distanse[i[0]]:
                distanse[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distanse[i] == INF:
        print('INF')
    else:
        print(distanse[i])
