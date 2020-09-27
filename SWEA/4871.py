'''
3
6 5

1 4
1 3
2 3
2 5
4 6

1, list(3,4)
2, list(3,5)
4, list(6)

1 6


7 4

1 6
2 3
2 6
3 5

2 5


9 9

2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8

1 9

6개의 노드 5개의 간선
1->6

S_list에서 S값에 해당하는 인덱스 접근

'''
V, E = map(int, input().split())
S_list = []
D_list = []
for i in range(E):
    t1,t2 = map(int,input().split())
    S_list.append(t1), D_list.append(t2)
S,D =  map(int,input().split())


