'''

8*8
1. 수평 2칸 수직 1칸
2. 수직 2칸 수평 1칸


'''
loc = input()
move = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
map = []
alp = ['a','b','c','d','e','f','g','h']

for i in range(8):
    map.append([(alp[i]+str(j+1)) for j in range(8)])
'''
[
['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'], 
 ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'], 
 ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8'], 
 ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8'], 
 ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'], 
 ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'], 
 ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'], 
 ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
 ]
'''
x = 0
y = 0
cnt = 0
for i in range(8):
    for j in range(8):
        if map[i][j] == loc:
            x = i
            y = j
            break
for d in range(8):
    dir = (x + move[d][0], y + move[d][1])
    if dir[0] <= 7 and dir[0] > -1 and dir[1] <= 7 and dir[1] > -1:
        cnt += 1
print(cnt)




