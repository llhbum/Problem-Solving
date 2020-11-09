'''
INPUT
4 4 2 1
1 2
1 3
2 3
2 4
'''
from collections import deque

n,m,k,x = map(int, input().split())
G = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int, input().split())
    G[s].append(e)

distance = [-1] *(n+1)
distance[x] = 0

q = deque([x])
while q:
    node = q.popleft()
    for next_node in G[node]:
        if distance[next_node] == -1:
            distance[next_node] = distance[node] + 1
            q.append(next_node)
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)




