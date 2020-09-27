"""
각 문자의 개수를 []로 묶어서 set

"""



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = list(input())
    i = 0
    while 1:
        if i == len(s) - 1:
            break
        if s[i] == s[i + 1]:
            str1 = s[0:i]
            str2 = s[i + 2:]
            s = str1 + str2
            i = 0
        else:
            i += 1
    print(f'#{test_case} {len(s)}')