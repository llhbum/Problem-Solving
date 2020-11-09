#DFS 메서드 정의
def dfs(G, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in G[v]:
        if not visited[i]:
            dfs(G, i, visited)

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

dfs(G,1,visited)