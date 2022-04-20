from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect(array, right_value)
    left_index = bisect(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())

array = list(map(int, input().split()))

count = list(map(int, input().split()))

if count == 0:
    print(-1)
else:
    print(count)