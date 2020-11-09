'''
INPUT
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''
def find_union(parent, x):
    if parent[x] != x:
        parent[x] = find_union(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_union(parent, a)
    b = find_union(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parnet = [0] * (n+1)
for i in range(n+1):
    parnet[i] = i

edges = []
result = 0

for i in range(m):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()
last = 0
for edge in edges:
    cost, a ,b = edge

    if find_union(parnet, a) != find_union(parnet, b):
        union_parent(parnet, a, b)
        result += cost
        last = cost
print(result - last)
