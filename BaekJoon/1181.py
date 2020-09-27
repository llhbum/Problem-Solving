'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

예제 입력 1
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

예제 출력 1
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

'''

#문자열 개수 입력받기
n = int(input())
n_list = []

#문자열 개수만큼 for문을 돌려 n_list에 입력받은 문자열 삽입
for i in range(n):
    n_list.append(input())

# set을 이용해서 중복제거 후 리스트화
voca_list = list(set(n_list))

# 튜플 이용해서 (문자열길이, 문자열)을 배열에 삽입
sort_voca_list = []
for i in voca_list:
    sort_voca_list.append([len(i),i])

# 배열 튜플에 첫번쨰에 저장된 문자열길이를 이용해서 sort
sort_voca_list.sort()

# 배열 튜플에 저장된 문자열만 출력
for j in range(len(sort_voca_list)):
    print(sort_voca_list[j][1])

