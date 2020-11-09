
def solution(tickets):
    route = {}
    #{
    # 'ICN': ['SFO', 'ATL'],
    # 'SFO': ['ATL'],
    # 'ATL': ['SFO', 'ICN']
    # }

    for (start, end) in tickets:
        route[start] = route.get(start, []) + [end]
        for r in route.keys():
            route[r].sort(reverse=True)

    st = ['ICN']
    path = []


    while st:
        top = st[-1]
        if top not in route or len(route[top]) == 0:
            path.append(st.pop())
        else:
            st.append(route[top][-1])
            route[top] = route[top][:-1]
    path.reverse()
    answer = path
    return answer
