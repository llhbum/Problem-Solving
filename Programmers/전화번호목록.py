# sort, in 방식
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer= False
            break
    return answer



# hash방식
def solution2(phone_book):
    answer = True
    hash_map = {}
    # 해쉬에 phone_number 처리
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

if __name__ == '__main__':
    #
    n_list = list(input())
    print(n_list)
    print(solution(n_list))

    a = ['223123123','1234512121212','123456']
    a.sort(key=len)
    print(a)


