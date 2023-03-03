# https://leetcode.com/problems/min-cost-climbing-stairs/description/

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         dy = [0]*(n+1)
#         dy[0] = 0
#         dy[1] = 0
#
#         for i in range(2, n+1):
#             dy[i] = min(dy[i-1] + cost[i-1], dy[i-2] + cost[i-2])
#         return dy[n]


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         size = len(cost)
#         minCost = [cost[0], cost[1]] + [float('inf')] * (size - 2)
#         # 1, 100, 1, 1, 1, 100, 1, 1, 100, 1
#         # 1, 100, 2, 3, 3, 103, 4, 5, 104, 6
#         for i in range(2, len(cost)):
#             minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
#
#         return min(minCost[size-1], minCost[size-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        minCost = [cost[0], cost[1]] + [float('inf')] * (size - 2)

        def DFS(pos):
            if minCost[pos] == float('inf'):
                minCost[pos] = cost[pos] + min(DFS(pos - 1), DFS(pos - 2))

            return minCost[pos]

        return min(DFS(size-1), DFS(size-2))