from collections import deque


def chardiff(a, b):
    cmp = zip(a, b)
    cnt = 0
    for x, y in zip(a, b):
        if x != y:
            cnt += 1
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    answer = 0

    visited = dict()
    lenwords = len(begin)
    q = deque()
    q.append((begin,0))
    visited[begin] = True
    while q:
        cur, l = q.popleft()
        for w in words:
            if chardiff(cur,w) and w not in visited:
                q.append((w,l+1))
                visited[w] = True
                if w == target:
                    answer = l + 1
    return answer


'''
hit => cog
hit -> hot -> dot -> dog -> cog


begin에서 words에 있는 글자중 한글자만 바꿔서 맞춰야함

'''