user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]





if __name__ == '__main__':
    N_user = len(user_id)
    N_ban = len(banned_id)
    temp = {}


    # for i in range(N_ban):
    #     t = banned_id.count(banned_id[i])
    #     for j in range(N_user):
    #         if len(user_id[j]) != len(banned_id[i]):
    #             pass
    #         else:
    #             cnt = 0
    #             for l in range(len(banned_id[i])):
    #                 if user_id[j][l] == banned_id[i][l]:
    #                     cnt+=1
    #             temp[user_id[j]] = cnt
    # # print(temp)
    # # tList_max = max(temp)
    # # max_cnt = temp.count(tList_max)
    # # print(max_cnt)
    # print(temp)





