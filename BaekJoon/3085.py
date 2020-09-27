# '''
# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
#
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
#
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
#
# 다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
#
# 사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.
#
# 출력
# 첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
#
# 예제 입력 1
# 5
# YCPZY
# CYZZP
# CCPPP
# YCYZC
# CPPZZ
# 4*5
# 4*5
# n*(n-1)+n*(n-1)
#
# 예제 출력 1
# 4
# 힌트
# 4번 행의 Y와 C를 바꾸면 C사탕 네 개를 먹을 수 있다.
# '''
#
#
#
#
#
#
#
#
#
#
#
# global max_cnt
# max_cnt = 0
#
# T_array= []
# line = int(input())
# for i in range(line):
#     temp = ""
#     temp = input()
#     temp_list = []
#     temp_list = list(temp)
#     T_array.append(temp_list)
#
# def move():
#     global max_cnt
#     for row in range(line):
#         for col in range(line):
#             if col+1 < line:
#                 T_array[row][col], T_array[row][col+1] = T_array[row][col+1], T_array[row][col]
#                 max_cnt = search()
#                 T_array[row][col+1], T_array[row][col] = T_array[row][col], T_array[row][col+1]
#
#     for row in range(line):
#         for col in range(line):
#             if col+1 < line:
#                 T_array[col][row], T_array[col+1][row] = T_array[col+1][row], T_array[col][row]
#                 max_cnt = search()
#                 T_array[col][row], T_array[col+1][row] = T_array[col+1][row], T_array[col][row]
#
#     return max_cnt
#
# def search():
#     global max_cnt
#     for row in range(line):
#         for col in range(line):
#             c_row_cnt = 0
#             p_row_cnt = 0
#             z_row_cnt = 0
#             y_row_cnt = 0
#
#             c_col_cnt = 0
#             p_col_cnt = 0
#             z_col_cnt = 0
#             y_col_cnt = 0
#
#
#             if T_array[row][col] == 'C':
#                 c_row_cnt += 1
#             elif T_array[row][col] == 'P':
#                 p_row_cnt += 1
#             elif T_array[row][col] == 'Z':
#                 z_row_cnt += 1
#             elif T_array[row][col] == 'Y':
#                 y_row_cnt += 1
#             elif T_array[col][row] =='C':
#                 c_col_cnt += 1
#             elif T_array[col][row] == 'P':
#                 p_col_cnt += 1
#             elif T_array[col][row] == 'Z':
#                 z_col_cnt += 1
#             elif T_array[col][row] == 'Y':
#                 y_col_cnt += 1
#             temp_cnt = max(c_row_cnt,z_row_cnt,p_row_cnt,y_row_cnt,c_col_cnt,p_col_cnt,z_col_cnt,y_col_cnt)
#             if temp_cnt > max_cnt:
#                 return temp_cnt
#             else:
#                 return 0
#
#
#
# print(move())


'''
N * N 행렬(이차원 배열)등장
1. 입력을 받아 2차원 배열 완성
2. 행,열 기준 N-1번 바꾸는 경우의 수 존재 -> for문, 1번 바꿀때 마다 검사
3. 바꾸면 사탕의 최대 개수 검사(행,렬) ->  연속된 색깔을 어떻게 선별? -> 색깔 별로 변수를 만들어서 연속되면 +=1 해줌

5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
'''
C_cnt, P_cnt, Z_cnt, Y_cnt = 1, 1, 1, 1
def loop(N, N_list):
    for i in range(N):
        for j in range(N-1):
            row_search(N_list, i)
            col_search(N_list, j)
            #행검사
            N_list[i][j], N_list[i][j+1] = N_list[i][j+1], N_list[i][j]
            row_search(N_list,i)
            col_search(N_list,j)
            N_list[i][j+1], N_list[i][j] = N_list[i][j], N_list[i][j+1]
            # print(N_list[i][j])

            #열 검사
            N_list[j][i], N_list[j+1][i] = N_list[j+1][i], N_list[j][i]
            col_search(N_list, j)
            row_search(N_list, i)
            N_list[j+1][i], N_list[j][i] = N_list[j][i], N_list[j+1][i]


    # for i in range(N):
    #     for j in range(N-1):
    #         #열 검사
    #         N_list[j][i], N_list[j+1][i] = N_list[j+1][i], N_list[j][i]
    #         col_search(N_list, j)
    #         row_search(N_list, i)
    #         N_list[j+1][i], N_list[j][i] = N_list[j][i], N_list[j+1][i]
    #         print(N_list[j][i])

def row_search(N_list,l):
    global C_cnt
    global P_cnt
    global Z_cnt
    global Y_cnt
    temp_c, temp_p, temp_z, temp_y = 1, 1, 1, 1
    for i in range(len(N_list) - 1):
        if N_list[l][i] == N_list[l][i + 1]:
            if N_list[l][i] == 'C':
                temp_c += 1
            elif N_list[l][i] == 'P':
                temp_p += 1
            elif N_list[l][i] == 'Z':
                temp_z += 1
            elif N_list[l][i] == 'Y':
                temp_y += 1
    if C_cnt < temp_c:
        C_cnt = temp_c
    if P_cnt < temp_p:
        P_cnt = temp_p
    if Z_cnt < temp_z:
        Z_cnt = temp_z
    if  Y_cnt < temp_y:
        Y_cnt = temp_y

def col_search(N_list,l):
    global C_cnt
    global P_cnt
    global Z_cnt
    global Y_cnt
    temp_c, temp_p, temp_z, temp_y = 1, 1, 1, 1
    for i in range(len(N_list) - 1):
        if N_list[i][l] == N_list[i + 1][l]:
            if N_list[i][l] == 'C':
                temp_c += 1
            elif N_list[i][l] == 'P':
                temp_p += 1
            elif N_list[i][l] == 'Z':
                temp_z += 1
            elif N_list[i][l] == 'Y':
                temp_y += 1
    if C_cnt < temp_c:
        C_cnt = temp_c
    if P_cnt < temp_p:
        P_cnt = temp_p
    if Z_cnt < temp_z:
        Z_cnt = temp_z
    if  Y_cnt < temp_y:
        Y_cnt = temp_y

if __name__ == '__main__':
    N = int(input())
    N_list = [list(input()) for i in range(N)]
    loop(N, N_list)
    print(max(C_cnt, P_cnt, Z_cnt, Y_cnt))
    print(C_cnt, P_cnt, Z_cnt, Y_cnt)


'''
5
CPZCC
ZYCPZ
CYYPZ
ZPZCC
CCPYY
'''