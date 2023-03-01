# def climbing_stairs(n):
#     memo = {}
#

#     def dp(n):
#         if n == 1:
#             return 1
#
#         if n == 2:
#             return 2
#
#         if n not in memo:
#             memo[n] = dp(n-1) + dp(n-2)
#
#         return memo[n]
#
#     return dp(n)

def climbing_stairs(n):
    memo = {}

    if n == 1:
        return 1

    if n == 2:
        return 2

    if n not in memo:
        memo[n] = climbing_stairs(n-1) + climbing_stairs(n-2)

    return memo[n]

print(climbing_stairs[10])