s = input().upper()
s_list = list(set(s))
s_cnt = []
for i in s_list:
    cnt = s.count(i)
    s_cnt.append(cnt)

if s_cnt.count(max(s_cnt)) >= 2:
    print('?')
else:
    print(s_list[s_cnt.index(max(s_cnt))])