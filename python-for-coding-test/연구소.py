n,m = map(int,input().split())
G = []
for i in range(n):
    G.append(list(map(int, input().split())))
print(G)

'''
BFS로 2가 감염시킨 후 0의 값 리턴하는 함수 만들기
벽을 세울수 있는 3가지의 모든 경우의 수 

'''