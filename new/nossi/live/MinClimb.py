# https://leetcode.com/problems/min-cost-climbing-stairs/

# 시간복잡도 구하려면 시행횟수 구해야한다.
# 2 ** n의 시간복잡도 코드
# def minCostClimbingStairs(cost):
#     n = len(cost)
#
#     def dfs(n):
#         # basecase
#         if n == 0 or n == 1:
#             return 0
#         return min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
#
#     return dfs(n)
#
#
# # minCostClimbingStairs(cost = [10, 15, 20])
# print(minCostClimbingStairs(cost = [10, 15, 20]))


# 메모이제이션 활용
# 2 ** n의 시간복잡도 코드
def minCostClimbingStairs(cost):
    n = len(cost)

    memo = {}

    def dfs(n):
        # basecase
        if n == 0 or n == 1:
            return 0

        # n번째 도달하는 최소비용 구한게 없으면(not in) 누군가가 뭘 해줘야 한다.
        if n not in memo:
            memo[n] = min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])
        return memo[n]

    return dfs(n)


# minCostClimbingStairs(cost = [10, 15, 20])
print(minCostClimbingStairs(cost = [10, 15, 20]))

