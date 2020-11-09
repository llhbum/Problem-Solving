from collections import *

#BFS 정의
def bfs(G, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in G[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

G = [
    [],
    [2,3,8],
    [1, 7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(G,1,visited)