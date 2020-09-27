import heapq
k = 7
sco = [1, 2, 3, 9, 10, 12]
# sco = [7]
heap = []
for i in sco:
    heapq.heappush(heap,i)

# cnt = 0
# while True:
#     if sco[0] >= k:
#         print(cnt)
#         break
#     elif len(sco) <= 1:
#         print(-1)
#         break
#     else:
#         temp = heapq.heappop(heap,0) + (heapq.heappop(heap,0) * 2)
#         cnt += 1
#         # sco.append(temp)

cnt = 0
while True:
    if heap[0] >= k:
        break
    elif len(heap) <= 1:
        cnt = -1
        break
    else:
        temp = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        cnt += 1
        heapq.heappush(heap,temp)
print(cnt)

def solution(scoville, K):
    heap = []
    answer = 0
    cnt = 0

    # scoville를 heap으로 변환
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if heap[0] >= K:
            break
        elif len(heap) <= 1:
            answer = -1
            break
        else:
            temp = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
            answer += 1
            heapq.heappush(heap, temp)
    return answer

if __name__ == '__main__':
    a =     solution(sco,k)
    print(a)

