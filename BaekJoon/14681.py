# 2 = -,+
# 1 = +,+
# 3 = -,-
# 4 = +,-

N = int(input())
M = int(input())

if N>0 and M>0:
    print(1)
elif N<0 and M>0:
    print(2)
elif N<0 and M <0:
    print(3)
elif N>0 and M<0:
    print(4)
else:
    print(0)