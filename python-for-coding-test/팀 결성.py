'''
INPUT
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

'''
def find_union(parent, x):
    if parent[x] != x:
        parent[x] = find_union(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_union(parent, a)
    b = find_union(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    bool ,a, b = map(int, input().split())
    if bool == 0:
        union_parent(parent, a, b)
    elif bool == 1:
        if find_union(parent, a) == find_union(parent, b):
            print('YES')
        else:
            print('NO')





