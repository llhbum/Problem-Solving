
# 범위 체크 0 < val < N , 길,목적지 경우
def check(y,x):
    return (0<= x < N and 0<= y < N and (Maze[y][x] == 0 or Maze[y][x] == 3))

def DFS(start_y,start_x):

    global rList
    global result
    #base case
    if Maze[start_y][start_x] == 3:
        result = 1
        return
    visited.append((start_y,start_x))
    for d in range(4):
        New_y = start_y + dy[d]
        New_x = start_x + dx[d]
        if check(New_y,New_x) and (New_y, New_x) not in visited:
            rList.append((New_y, New_x))
            DFS(New_y,New_x)


N = int(input())
# Maze에 입력미로 값을 이차원 배열로 만듬
Maze = [list(map(int, input())) for _ in range(N)]
#[[1, 3, 1, 0, 1],
# [1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1],
# [1, 0, 1, 0, 1],
# [1, 0, 0, 2, 1]]


for y in range(N):
    for x in range(N):
        if Maze[y][x] == 2:
            start_x,start_y = x,y
# 북동남서 방향으로 길이 있는지 체크 후 이동
dy = [-1,1,0,0]
dx = [0,0,-1,1]

visited = []
rList = []
result = 0
DFS(start_y,start_x)

print(result)
print(visited)
print(rList)

