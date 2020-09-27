
'''
1 1000 500
1 500
250 500 375
250 375 312
250 312 562/2 281
281 312 593/2 296
296 312

'''

'''
1. l,r,c를 구한다.
target이 
c>target -> r = c
c<target -> l = c

a_cnt, b_cnt 
400 
l = 1, r = 400 target = 300 
함수(r, c, target)
cnt = 0
while target != c:
l = 1
if c>target : r = c
elif c<target : l = c 

c = (r+l)/2
cnt +=1 

return cnt



'''



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    r, a_target, b_target = map(int, input().split())
    a_cnt, b_cnt = 0, 0


    def search(r, target):
        cnt = 1
        l = 1
        c = int((r + l) / 2)
        while target != c:

            if c < target:
                l = c
            elif c > target:
                r = c

            c = int((r + l) / 2)
            cnt += 1
        return cnt


    a_cnt = search(r, a_target)
    b_cnt = search(r, b_target)

    if a_cnt > b_cnt:
        result = 'B'
    elif a_cnt < b_cnt:
        result = 'A'
    else:
        result = 0

    print(f'#{test_case} {result}')
