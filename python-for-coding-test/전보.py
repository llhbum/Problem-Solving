'''
3 2 1
1 2 4
1 3 2
'''
import heapq
#도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
n, m, c = map(int,input().split())
INF = int(1e9)
G = [ [] for i in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    #도착지, 시간 순의 튜플로 저장
    G[x].append((y,z))
distance = [INF] * (n+1)




def dijktra(start):
    h = []

    heapq.heappush(h, (0,start))
    distance[start] = 0
    while h:
        dist, node = heapq.heappop(h)
        if distance[node] < dist:
            continue
        for i in G[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))

dijktra(c)

cnt = 0
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)
print(cnt - 1, max_distance)

