'''
1 = 상덕
2 = 중덕
3 = 하덕
4 = 콜라
5 = 사이다
'''
berger = []
bever = []
for i in range(5):
    if i < 3:
        berger.append(int(input()))
    else:
        bever.append(int(input()))
'''
[800, 700, 900]
[198, 330]
'''
minSet = berger[0] + bever[0] - 50
for i in range(len(berger)):
    for j in range(len(bever)):
        temp = berger[i] + bever[j] - 50
        if minSet > temp:
            minSet = temp
print(minSet)


