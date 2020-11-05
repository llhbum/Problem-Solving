import heapq

list = [1,3,5,7,9,2,4,6,8,0]
# 오름차순
def upheapsort(list):
    h = []
    result = []
    for value in list:
        heapq.heappush(h,value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = upheapsort(list)
print(result)

#내림차순
def downheapsort(list):
    h = []
    result = []
    for value in list:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-(heapq.heappop(h)))
    return result

result2 = downheapsort(list)
print(result2)