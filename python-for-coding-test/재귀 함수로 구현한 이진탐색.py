def binary_search(nList, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if nList[mid] == target:
        return mid
    elif nList[mid] > target:
        return binary_search(nList, target,start, mid-1)
    else:
        return binary_search(nList,target, mid+1, end)

n, target = list(map(int,input().split()))
nList = list(map(int, input().split()))

result = binary_search(nList, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)