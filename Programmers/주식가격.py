p = [1, 2, 3, 2, 3]
answer = []
# for i in range(len(p)-1): # 0,1,2,3
#     cnt = 0
#     for j in range(i+1,len(p)): # 1,2,3,4
#         if p[i] > p[j] :
#             answer.append(len(p) - j - 1)
#             break
#         else:
#             if cnt == (len(p) - i - 2):
#                 answer.append(cnt+1)
#             else:
#                 cnt += 1
# answer.append(0)
# print(answer)


# def solution(prices):
#     answer = []
#     for i in range(len(prices)-1):
#         cnt = 1
#         for j in range(i+1, len(prices)):
#             if prices[i] > prices[j]:
#                 answer.append(j - i)
#                 break
#             else:
#                 if cnt == (len(prices) -i - 1):
#                     answer.append(cnt+1)
#                 else:
#                     cnt += 1
#     answer.append(0)
#     return answer

def solution(prices):
    answer = []
    for i in range(len(prices)-1):

        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            else:
                if len(prices) - 1 == j:
                    answer.append(j - i)
    answer.append(0)
    return answer