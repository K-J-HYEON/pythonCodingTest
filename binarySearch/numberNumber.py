def count_by_value(array, x):

    n = len(array)

    a = first(array, x, 0, n - 1)

    if a == None:
        return 0

    b = last(array, x, 0, n - 1)

    
    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid

    elif array[mid] >= target:
        return first(array, target, start, mid - 1)

    else:
        return first(array, target, mid + 1, end)

    

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid

    elif array[mid] > target:
        return last(array, target, start, mid - 1)

    else:
        return last(array, target, mid + 1, end)

    
n, x = map(int, input().split())

array = list(map(int, input().split()))

# 값이 x인 데이터의 개수 계산
coubt = count_by_value(array, x)

if count == 0:
    print(-1)

else:
    print(count)