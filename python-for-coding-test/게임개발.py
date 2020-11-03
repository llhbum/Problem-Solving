'''
N*M

INPUT
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

'''
# 입력받기

Map = []
n, m = map(int,input().split())
x, y, startDir = map(int, input().split())
# Map
for _ in range(n):
    Map.append(list(map(int,input().split())))
    # [
    # [1, 1, 1, 1],
    # [1, 0, 0, 1],
    # [1, 1, 0, 1],
    # [1, 1, 1, 1]
    # ]
# 방문기록리스트
visited = [[False for _ in range(n)] for _ in range(m)]

#방향
dir = startDir

# 방향벡터
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 왼쪽으로 90도 회전 함수
def dir_90():
    global dir
    if dir == 3:
        dir = 0
    else:
        dir += 1

cnt = 0 # 이동cnt
turn_time = 0 # key point // 회전횟수
# while 문으로 조건이 만족될때 까지 계속해서 수행
while True:
    # 왼쪽 1한번 회전
    dir_90()
    #nx,ny 만들기
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 만약 이동칸이 육지이면서 방문한적이 없다면
    if Map[nx][ny] == 0 and visited[nx][ny] == False:
        # 방문처리
        visited[nx][ny] = True
        # 이동확정
        x = nx
        y = ny
        # 이동 카운터 + 1
        cnt += 1
        #회전 카운터 + 1
        turn_time = 0
    # 만약 바다이거나 방문한적이 있다면
    else:
        # 회전카운터만 + 1
        turn_time += 1
    # 만약 회전카운터가 = 4가 된다면
    if turn_time == 4:
        # 뒷칸으로 이동
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 만약 뒷칸이 육지이면
        if Map[x][y] == 0:
            # 이동 확정
            x = nx
            y = ny
            turn_time = 0
        # 만약 뒷칸이 바다이면
        else:
            # break로 while탈출 -> 종료
            break


print(cnt)


















