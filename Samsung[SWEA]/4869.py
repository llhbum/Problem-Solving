'''
방법1
20 * 10 ,10 * 20(전치행렬) 20 * 20

N값을 이용해서 20*N의 2차원 배열을 만듬


'''



def get(x):
    if x == N: # x == N의 값이 같아지면 1을 리턴
        return 1
    if x > N :
        return 0 # 범위를 벗어남 -> 버림
    return get(x + 10) + get(x + 20) * 2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    print(f'#{test_case} {get(0)}')

# 재귀함수를 이용해서 푼 문제
# get(x+20) * 2의 의미는 10이 들어갈 수 있는 가로의 경우도 생각해준것것