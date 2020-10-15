#정답
def solution(citations):
    citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l - i
    return 0

# 오답
def solution(citations):
    citations.sort(reversed(True))
    for i in range(len(citations)):
        if citations[i] <= i+1:
            return i+1
    return 0

#풀이
def solution(citations):
    citations.sort() # 오름차순으로 정렬 -> 내림차순 정렬은 함정인듯 ?
    l = len(citations) # citations의 길이를 l로 지정
    for i in range(l): #for문을 돌려서
        if citations[i] >= l-i: # l - i 보다 크거나 같은 citations[i]을 찾는다.
            return l - i # 조건에 부합하면 l - i를 리턴
    return 0 # 0을 리턴


