while True:
    line = []
    x, y, z = map(int, input().split())
    line.append(x)
    line.append(y)
    line.append(z)

    if x == 0 and y == 0 and z == 0:
        break
    else:
        max_line = max(line)
        line.remove(max_line)
        if pow(max_line, 2) == pow(line[0], 2) + pow(line[1], 2):
            print("right")
        else:
            print("wrong")
