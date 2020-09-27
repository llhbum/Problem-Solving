'''
1. n,m을 입력받고
2. 가로부터 찾기 -> for i<->i+m-1 같으면 회문비교
3. 다르면 계속 찾기
4. 세로는 가로세로 만 바꿔서 찾기
'''
def H(H_array,N,M):
    result = []
    result_str = ''
    for i in range(N):
        for j in range(N):
            if j + M - 1 >= N:
                break
            else:
                if H_array[i][j] == H_array[i][j + M - 1]:
                    tmp = ''
                    temp1 = ''
                    temp2 = ''

                    cnt = 0
                    for k in range(M):
                        if H_array[i][j + k] == H_array[i][j - k + M - 1]:
                            cnt += 1
                            temp1 += (H_array[i][j + k])
                            temp2 += (H_array[i][j - k + M - 1])

                        if cnt == int(M / 2) + 1:
                            if M % 2 == 0:
                                temp2 = temp2[len(temp2)-3::-1]
                            else:
                                temp2 = temp2[len(temp2)-2::-1]
                            tmp = temp1 + temp2
                            result.append(tmp)
                            result_str = ' '.join(map(str, result[0:M]))
                            if len(result_str) == M:
                                return result_str


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    H_array = []

    # 2차원 배열로 만듬
    for _ in range(N):
        H_array.append(list(input()))

    # 전치행렬
    HT_array = [[e for e in t] for t in zip(*H_array)]

    result = H(H_array,N,M)
    if result == None:
        result = H(HT_array,N,M)

    print(f'#{test_case} {result}')



