'''
정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중엥서 3이 하나라도 포함되는 모든 경우의 수를 구하는 문제

* 00시 59분 59초까지 몇번의 3포함 시간이 나오는지 계산 * N



INPUT
5
'''

n = int(input())
cnt = 0
for si in range(n+1):
    for boon in range(60):
        for cho in range(60):
            if '3' in str(si) + str(boon) + str(cho):
                cnt += 1
print(cnt)
