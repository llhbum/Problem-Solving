'''
1. str1, str2를 리스트로 입력받는다.

'''




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l1 = list(input())
    l2 = list(input())
    result = 0
    for i in range(len(l2)):
        if l2[i] == l1[0]:
            cnt = 0
            for j in range(len(l1)):

                if l2[i + j] == l1[j]:
                    cnt += 1
                if cnt == len(l1):
                    result += 1
                if (i + j) >= len(l2) - 1:
                    break
    print(f'#{test_case} {result}')