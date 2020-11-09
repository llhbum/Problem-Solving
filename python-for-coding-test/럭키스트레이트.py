n = input()
n_1 = n[:len(n)//2]
n_2 = n[len(n)//2:]

n1_list = list(map(int,n_1))
n2_list = list(map(int,n_2))

if sum(n1_list) == sum(n2_list):
    print('LUCKY')
else:
    print('READY')