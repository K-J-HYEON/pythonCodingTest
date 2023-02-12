# https://www.acmicpc.net/problem/2512

from sys import stdin
input = stdin.readline
N = int(input())
budget_list = list(map(int, input().split()))
total_budget = int(input())
start, end = 0, max(budget_list)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for each_budget in budget_list:
        if each_budget <= mid:
            sum += each_budget

        else:
            sum += mid

    if sum <= total_budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)
