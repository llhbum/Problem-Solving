'''
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.
입출력 예
s	return
abcde	c
qwer	we

'''

#답
def solution(s):
    answer = ''
    s_len = len(s)
    targetIndex = s_len // 2
    if s_len % 2 == 0:  # 짝수
        answer = s[targetIndex - 1:targetIndex + 1]
    else:  # 홀수
        answer = s[targetIndex]
    return answer

#풀이
def solution(s):
    answer = ''
    s_len = len(s) # s의 길이를 구하라
    targetIndex = s_len // 2 # s_len을 2로 나누어  targetIndex를 구하라
    if s_len % 2 == 0:  # 짝수일떄
        answer = s[targetIndex - 1:targetIndex + 1] #targetIndex로 -1. +1로 가운데 두글자 구하기
    else:  # 홀수일떄
        answer = s[targetIndex] #targetIndex로 가운데글자구하기
    return answer
