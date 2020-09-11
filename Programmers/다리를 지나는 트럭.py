def solution(bridge_length, weight, truck_weights):
    time = 0 # 시간을 0으로
    q = [0] * bridge_length # 다리의 길이만큼 0을 채운 큐 생성

    while q : # 큐에 값이 없을 때 까지 반복
        time += 1 # 시간에 + 1
        q.pop(0) # 큐에서 값하나는 pop한다.
        if truck_weights: # 만약 truck_weights에 값이 있다면
            if sum(q) + truck_weights[0] <= weight: # 만약 q의 모든 값 + truck_weights[0]의 값이 <= 무게 기준 이면
                q.append(truck_weights.pop(0)) # 큐에 truck_weights.pop(0)한 값을 append 한다.
            else: # 만약 무게 기준 이하라면
                q.append(0) # 큐에 0을 append 한다.
    return time # time을 리턴한다.


