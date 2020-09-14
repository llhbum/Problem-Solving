def solution(citations):
    citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l - i
    return 0

# 오답
# def solution(citations):
#     citations.sort()
#     l = len(citations)//2
#     if citations[l] == len(citations) - l:
#         return len(citations) - l
#     else:
#         return len(citations) - l - 1
