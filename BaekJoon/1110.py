'''
0<= N <=99
10>N : 0N

2(6) = 2+6=0(8)
6(8) = 6+8=1(4)
8(4) = 8+4=1(2)
4(2) = 4+2=0(6)
26

4번

26 split 2+6 = 8 if 나뉠게 있으면 나누고 없으면 그냥 둬
뒤에 숫자라 결과의 뒤에 숫자라 str로 바꿔서 더해 ->비교 26이랑 아니면 반복 -> int로 바꿔
'''

N = int(input())
check = N
newNum = 0
cnt = 0
while True:
    temp = N // 10 + N % 10
    newNum = (N % 10) * 10 + temp % 10
    cnt += 1
    if newNum == check:
        break
    else:
        N = newNum
print(cnt)
