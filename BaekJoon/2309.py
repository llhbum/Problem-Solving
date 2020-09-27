# 9난쟁이의 키를 받을 리스트
n_list = []
# for문을 돌려서 9난쟁이의 키를 int로 받아서 n_list에 append시킨다.
for i in range(9):
    n_list.append(int(input()))

# 결과를 오름차순으로 출력해야하므로 미리 sort()시킨다.
n_list.sort()
# 전체키의 합을 res에 저장한다.
res = sum(n_list)

"""
방법이 2가지다.
첫 번째 9개중 7개씩만 뽑아서 100을 만들지
두 번쨰 9개중 2개씩 뽑은 후 그것만 빼고 더해서 100을 만들지 -> 후자를 선택했다. 
"""

# 2개씩 추출해야하므로 2중 for문을 사용한다. 변수는 n_1, n_2로한다.
for n_1 in range(9):
    for n_2 in range(n_1+1,9):
        # res에서 선택된 두 키가 == 100 이면,
        if res - n_list[n_1] - n_list[n_2] == 100:
            # for 문을 총 키의 수만큼 돌려준다.
            for idx in range(len(n_list)):
                # 인덱스 값이 n_1, n_2와 같으면 continue로 넘기고
                if idx == n_1 or idx == n_2 : continue
                # 나머지 경우는 출력해준다. !위에 sort했기때문에 오름차순으로 출력된다.
                else: print(n_list[idx])
            exit()

