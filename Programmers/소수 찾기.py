# 답

import itertools

def sosu(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        tempL = list(map(''.join, itertools.permutations(numbers, i)))
        for j in tempL:
            j = int(j)
            if sosu(j) == True:
                answer.append(j)
    return len(set(answer))

# 풀이

import itertools #새롭게 배운 itertools - >  iterable의 원소로 순열과 조합을 구하는 방법// permutations사용할 것이다.

def sosu(n): # 소수를 구하는 함수 return타입은 boolean이다.
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = [] # 조건에 만족하는 값을 담을 리스트

    for i in range(1, len(numbers) + 1): #permutations을 이용할 것이 때문에 원하는 자릿수인 1...n 까지 출력해줄 for문이 필요하다.
        tempL = list(map(''.join, itertools.permutations(numbers, i))) # 자릿수를 이용해서 numbers를 순열 list로 생성
        for j in tempL: # tempL에서 값을 뽑아와
            j = int(j) # 정수로 변환후
            if sosu(j) == True: # 소수감별 함수를 불러와 검사후 True이면
                answer.append(j) #answer리스트에 append시켜준다.
    return len(set(answer)) # 중복값이 발생하므로 set이용 후 len로 개수를 세어서 리턴시킨다.