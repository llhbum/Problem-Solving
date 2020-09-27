'''

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다.
둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
#계수정렬

import sys

n_cnt =int(input())
#계수정렬로 풀어야 하므로 모든 리스트의 길이를 10001으로 값은 0으로 채워준다.
n_list = [0] * 10001

for i in range(n_cnt):
    # input으로 받지말고 stdin으로 빠르게 받는다.
    input_val = int(sys.stdin.readline())
    # 받은 숫자는 인덱스가 되고, 인덱스에 해당하는 값에 +1을 해준다.
    n_list[input_val] = n_list[input_val] + 1

# 인덱스에 접근하기 위해서 리스트의 길이만큼 for문을 돈다.
for i in range(len(n_list)):
    # 인덱스에 해당하는 값이 0이 아닌 수를 if문을 통해서 골라낸다.
    if n_list[i] != 0:
        # 해당하는 값만큼 인덱스값을 출력한다.
        for j in range(n_list[i]):
            print(i)
    #if문에 해당하지 않는 경우는 모두 pass한다.
    else:
        pass