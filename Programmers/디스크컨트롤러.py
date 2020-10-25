'''
제 설명
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.
Screen Shot 2018-09-13 at 6.34.58 PM.png

한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.
Screen Shot 2018-09-13 at 6.38.52 PM.png

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면
Screen Shot 2018-09-13 at 6.41.42 PM.png

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
입출력 예
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.
'''


jobs = [[0, 3], [1, 9], [2, 6]]
# 시작sec로 오름차순 정렬

# jobs.sort(key= lambda item:item[0])
# ans = jobs[0][1]
# result = []
# result.append(ans)
# for i in range(1,len(jobs)):
#     ans = ans + jobs[i][1] - 1
#     result.append(ans)
#
# print(result)
#
# result_sum = int(sum(result) / len(result))
# print(result_sum)


#답
def solution(jobs):
    import heapq
    jobs.sort()
    answer = 0
    n = 0
    time = jobs[0][0]
    pq = []

    while jobs:
        (request, expend) = jobs.pop(0)
        n += 1
        time += expend
        answer += (time - request)

        while jobs and jobs[0][0] < time :
            (request, expend) = jobs.pop(0)
            heapq.heappush(pq, (-expend, request))

        while pq:
            (expend, request) = heapq.heappop(pq)
            jobs.insert(0, [request, -expend])

    answer //=n
    return answer

#풀이
def solution(jobs):
    import heapq

    # 1. jobs 정렬
    jobs.sort()
    answer = 0
    n = 0
    # 2. 최초 시간 설정
    time = jobs[0][0]
    # 3. 우선순위 큐 생성
    pq = []

    # 4. job이 빌 떄까지 다음을 반복합니다.
    while jobs:
        # 1. jobs의 첫 원소를 꺼내옵니다.
        (request, expend) = jobs.pop(0)
        # 2. n에 1을 더해줍니다.
        n += 1
        # 3. time에 소요 시간 expend를 더해줍니다.
        time += expend
        # 4. answer에 현재 시간 time에서 요청 시간 request를 뺸 값을 더해줍니다.
        answer += (time - request)

        # 5. jobs가 비지 않고, jobs[0][0]일 떄 다음을 반복합니다.
        while jobs and jobs[0][0] < time:
            # 1. jobs의 첫 원소를 꺼내옵니다.
            (request, expend) = jobs.pop(0)
            # 2. 해당 원소를 expend 기준으로 pq에다 저장합니다.
            heapq.heappush(pq, (-expend, request))

        # 6. pq가 빌 떄까지 다음을 반복합니다.
        while pq:
            # 1. pq에서 원소를 꺼냅니다.
            (expend, request) = heapq.heappop(pq)
            # 2. jobs에 첫 원소로 저장합니다.
            jobs.insert(0, [request, -expend])

    # 5. answer에 n을 나눠준 몫을 저장하고 반환합니다.
    answer //= n
    return answer