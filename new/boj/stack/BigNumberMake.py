# https://www.acmicpc.net/problem/2812

# import sys
# input = sys.stdin.readline
#
# n,k = map(int, input().split())
# numbers = input().rstrip()
# stack = []
#
# for number in numbers:
#     while stack and stack[-1] < number and k > 0:
#         stack.pop()
#         k -= 1
#
#     stack.append(number)
#
# if k > 0:
#     print(''.join(stack[:-k]))
# else:
#     print(''.join(stack))
#

# sol2
N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
    stack.append(num[i])

print(''.join(stack[:N-K]))