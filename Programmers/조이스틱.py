'''
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
'''
# 답
def solution(name):
    # 1. 알파벳을 맞추는 최소 횟수를 저장하는 배열 m을 만듭니다.
    m = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer = 0
    where = 0

    # 2. 위치 where를 0부터 시작해서, 다음을 반복합니다.
    while True:
        # 1. m[where]를 answer에 더합니다
        answer += m[where]
        # 2. m[where]를 0으로 만듭니다.
        m[where] = 0

        # 3. 만약, 현재 m이 모두 0이라면, 반복을 멈춥니다.
        if sum(m) == 0:
            break

        # 4. 3이 만족하지 않을 때, left, right를 1로 만듭니다.
        left, right = (1, 1)

        # 5. m[where-left] <= 0일 때까지, left를 1씩 증가시킵니다.
        while m[where - left] <= 0:
            left += 1
        # 6. m[where+right] <= 0일 때까지 right를 1씩 증가시킵니다.
        while m[where + right] <= 0:
            right += 1

        # 7. left, right를 비교합니다.
        # 7-1. left < right 라면, answer에 left를 더하고, where에 -left를 더합니다.
        # 7-2. 반대라면, answer에 right를 더하고 where에 right를 더합니다.
        answer += left if left < right else right
        where += -left if left < right else right

    return answer
#오답
# def solution(name):
#     alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     alp = list(alp)
#     name = list(name)
#     answer = 0
#
#     for i in range(len(name)):
#         if name[i] == 'A':
#             pass
#         else:
#             for j in range(len(alp)):
#                 if name[i] == alp[j]:
#                     print(name[i])
#                     if j >= 13:
#                         answer += 26 - j
#
#                     else:
#                         answer += j
#
#     notA_list = []
#     for i in range(len(name)):
#         if name[i] == 'A':
#             pass
#         else:
#             notA_list.append(i)
#
#     while True:
#         if len(notA_list) < 2:
#             break
#         else:
#             if len(notA_list) == 2:
#                 answer += 1
#                 break
#             else:
#                 for i in range(len(notA_list)):
#                     left_ = abs(notA_list[i] - notA_list[i - 1])
#                     right_ = abs(notA_list[i] - notA_list[i + 1])
#
#                     if len(notA_list) == left_ + 1:
#                         left_ = 1
#                     if len(notA_list) == right_ + 1:
#                         right_ = 1
#
#                     if left_ < right_:
#                         answer += left_
#                         notA_list.pop(i)
#                         break
#                     else:
#                         answer += right_
#                         notA_list.pop(i)
#                         break
#     return answer
