# https://www.acmicpc.net/problem/7795

import sys
input = sys.stdin.readline

def bin_search(target, data):
    start = 0
    end = len(data) - 1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for i in A:
        cnt += bin_search(i, B) + 1

    print(cnt)


# for _ in range(int(input())):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#
#     A.sort()
#     B.sort()
#
#     count = 0
#     pair = 0
#
#     for i in range(N):
#         while True:
#             if count == M or A[i] <= B[count]:
#                 pair += count
#                 break
#             else:
#                 count += 1


    # print(pair)
