# https://leetcode.com/problems/coin-change/
# 최단거리 문제 => BFS? => 10**9 => 완전탐색
# bfs는 시간초과가 나옴
# 메모리 사용 DP를 이용해서 효율성 증대?
# 즉 처음 dfs bfs 완전탐색이였다가 => 메모리 사용 효율성 증대할 수 있는 DP로 풀수 있구나

# sol 시간초과 나는 코드 dfs bfs
# def coinChange(coins, amount):
#     def dfs(amount):
#         if amount == 0:
#             return 0
#
#         if amount < 0:
#             return -1
#
#         min_ret = float('inf')
#
#         # min_ret = 10001
#         for coin in coins:
#             next_amount = amount - coin
#             ret = dfs(next_amount)
#             if ret == -1:
#                 continue
#             min_ret = min(min_ret, ret)
#
#         return min_ret + 1
#     return dfs(amount)
#
# print(coinChange([1, 2, 5], amount=11))


# sol 2 DP
# 10000 ^ 12
# 10000 * 12
# Memoization
def coinChange(coins, amount):
    memo = {}

    def dfs(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        min_ret = float('inf')
        # min_ret = 10001
        for coin in coins:
            next_amount = amount - coin

            if next_amount not in memo:
                memo[next_amount] = dfs(next_amount)
            ret = memo[next_amount]

            if ret == -1:
                continue
            min_ret = min(min_ret, ret)

        return min_ret + 1
    return dfs(amount)

print(coinChange([1, 2, 5], amount=11))