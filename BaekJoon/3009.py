point = [list(map(int, input().split())) for _ in range(3)]
result_point = [0 for _ in range(2)]

for i in range(len(point) - 1):
    for j in range(i + 1, len(point)):
        if point[i][0] == point[j][0]:
            result_point[0] = point[3 - i - j][0]
        if point[i][1] == point[j][1]:
            result_point[1] = point[3 - i - j][1]

for n in range(len(result_point)):
    print(result_point[n], end=' ')
