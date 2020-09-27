"""
1. set을 이용해서 str1의 중복을 제거해준다.
2. str1을 딕셔너리로 만들어서 str1의 값들을 str2와 비교한다.
3. 비교해서 == 값은 val:+1을 해준다.
4. val중 가장 큰 값을 뽑는다.
"""




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    strList1 = list(set(input()))
    strList2 = list(input())
    mydic = {}

    for i in range(len(strList1)):
        cnt = 0
        for j in range(len(strList2)):
            if strList1[i] == strList2[j]:
                cnt += 1
        mydic[strList1[i]] = cnt

    max_val = max(mydic.values())
    print(f'#{test_case} {max_val}')
