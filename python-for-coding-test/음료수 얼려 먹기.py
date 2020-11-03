
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if G[x][y] == 0:
        G[x][y] = 1

        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x-1,y)

        return True
    return False

# G 만들기
n, m = map(int, input().split())
G = []
for i in range(n):
    G.append(list(map(int, input())))
'''
4 5
00110
00011
11111
00000
'''
print(G)
#
# [
# [0, 0, 1, 1, 0],
# [0, 0, 0, 1, 1],
# [1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0]
# ]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)