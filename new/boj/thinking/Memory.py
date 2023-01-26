import sys
input = sys.stdin.readline

def binary_search(j, r, nums1, num):
    while j <= r:
        mid = (j + r) // 2

        if nums1[mid] == num:
            return 1
        elif nums1[mid] < num:
            j = mid + 1
        else:
            r = mid - 1
    return 0

t = int(input())

for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums1.sort()
    m = int(input())
    nums2 = list(map(int, input().split()))
    for num in nums2:
        print(binary_search(0, n-1, nums1, num))