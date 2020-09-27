N = int(input())

array_2 = [[' ' for _ in range(N)] for _ in range(2)]



for i in range(N):
    if i % 2 == 0 :
        array_2[0][i] = "*"
    elif i % 2 == 1:
        array_2[1][i] = '*'

for i in range(N):
    for i in range(2):
        for j in range(N):
            print(array_2[i][j] , end='')
        print()



"""
2
00 01 
10 11 


0 01
1 01


3
00 01 02
10 11 12

4
00 01 02 03
10 11 12 13

5 
00 01 02 03 04
10 11 12 13 14

"""
