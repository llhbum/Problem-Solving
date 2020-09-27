height = int(input())
for height_val in range(height):
    for star_cnt in range(height_val+1):
        print('*',end='')
    print()