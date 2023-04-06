# https://www.acmicpc.net/problem/10816

# import sys
# from collections import defaultdict
# input = sys.stdin.readline
#
# n = int(input())
# cards = list(map(int, input().split()))
# cards_cnt = defaultdict(int)
#
# for c in cards:
#     cards_cnt[c] += 1
#
# # print(cards_cnt)
# m = int(input())
# check = list(map(int, input().rsplit()))
#
# for c in check:
#     l, r = 0, len(cards)
#     while l <= r:
#         mid = (l + r) // 2
#         if mid < c:
#             l = mid + 1
#         elif mid > c:
#             r = mid - 1
#         else:
#             break
#
#     print(cards_cnt[c], end=' ')


# N = int(input())
# cards = list(map(int, input().split()))
# cards.sort()
# cardsDic = {}
#
# for c in cards:
#     if c not in cardsDic:
#         cardsDic[c] = 1
#
#     else:
#         cardsDic[c] += 1
#
# M = int(input())
# nums = list(map(int, input().split()))
#
# for n in nums:
#     start = 0
#     end = N -1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if cards[mid] == n:
#             break
#
#         if cards[mid] < n:
#             start = mid + 1
#
#         else:
#             end = mid - 1
#
#     if cards[mid] == n:
#         print(cardsDic[n], end=" ")
#
#     else:
#         print(0, end = " ")

import sys
input = sys.stdin.readline

N = int(input())
a = map(int, input().split())

hash = {}
for num in a:
    hash[num] = hash.setdefault(num, 0) + 1

M = int(input())
b = map(int, input().split())
for num in b:
    print(hash.setdefault(num, 0), end = ' ')