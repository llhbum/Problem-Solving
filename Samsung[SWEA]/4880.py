# from builtins import range
#
#
# # def win(dic):
# #     dic_key = dic.keys()
# #     if dic[0]==dic[1]:
# #         minVal = min(dic_key[0],dic_key[1])
# #         return minVal
# #     else:
# #         '''
# #         1 = 가위, 2 = 바위, 3 = 보
# #         '''
# #         if dic[0] == 1 and dic[1] == 2:
# #             return dic[2]
# #         elif dic[0] == 1 and dic[1] == 3:
# #             return dic[1]
# #         elif dic[0] == 2 and dic[1] == 3:
# #             return dic[3]
# #
# #
# # def splite():
# #     # 목적 : 딕셔너리가 들어왔을 떄
# #
# #
# #
# # # 전처리과정
# # N = int(input())
# # dic={}
# # n_list = list(map(int,input().split()))
# # n_list2= enumerate(n_list)
# # for key,val in n_list2:
# #     dic[key] = val
# # key = dic.keys()
# # val = dic.values()
# # print(win(dic))
# def verse(list):
#     list1 = list[0:((list[0] + len(list)) // 2)]
#     list2 = list[((list[0] + len(list)) // 2): len(list) + 1]
#     if len(list) == 1:
#         return [list[0]]
#     # 가위바위보의 승자 인덱스 출력
#     elif len(list) == 2:
#         if (list[0] == 1 or list[1] == 1) and(list[0] == 2 or list[1] == 2):
#             return [2]
#         elif (list[0] == 1 or list[1] == 1) and(list[0] == 3 or list[1] == 3):
#             return [1]
#         elif (list[0] == 3 or list[1] == 3) and(list[0] == 2 or list[1] == 2):
#             return [3]
#         else:
#             return [list[0]]
#     elif len(list)>2:
#         return verse(list)
#
#
#
#
#
# N = int(input())
#
# n_list = list(map(int,input().split()))
# print(n_list)
#
# result = verse(n_list)
# print(n_list.index(result)+1)
#
# list1 = list[0:((list[0] + len(list)) // 2)]
# list2 = list[((list[0] + len(list)) // 2): len(list) + 1]



def Game(start_idx, end_idx):
    if start_idx == end_idx:
        return start_idx
    man1 = Game(start_idx,(start_idx+end_idx)//2)
    man2 = Game((start_idx+end_idx)//2+1,end_idx)

    if (cards[man2] == 1 and cards[man1] == 3 or
        cards[man2] == 2 and cards[man1] == 1 or
        cards[man2] == 3 and cards[man1] ==2 ):
        return man2
    else:
        return man1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, (('0 ' + input())).split()))
    print(f'#{test_case} {Game(1, N)}')
