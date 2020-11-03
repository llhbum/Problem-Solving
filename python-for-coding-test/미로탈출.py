# '''
# 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# '''

from collections import deque


def dfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 초과 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽 무시
            if G[nx][ny] == 0:
                continue
            if G[nx][ny] == 1:
                G[nx][ny] = G[x][y] + 1
                q.append((nx,ny))
    return G[n-1][m-1]


n, m = map(int, input().split())
G = []
for i in range(n):
    G.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = dfs(0,0)
print(result)
# 10