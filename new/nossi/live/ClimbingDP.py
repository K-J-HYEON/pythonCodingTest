# def climbing_stairs(n):
#     memo = {}
#
#     if n == 1:
#         return 1
#
#     if n == 2:
#         return 2
#
#     if n-1 not in memo:
#         memo[n-1] = climbing_stairs(n-1)
#
#     if n-2 not in memo:
#         memo[n-2] = climbing_stairs(n-2)
#
#     return memo[n-1] + memo[n-2]

# def climbing_stairs(n):
#     memo = {}
#
#     if n == 1:
#         return 1
#
#     if n == 2:
#         return 2
#
#     if n in memo:
#         return memo[n]
#
#     if n not in memo:
#         memo[n] = climbing_stairs(n-1) + climbing_stairs(n-2)
#     return climbing_stairs(n-1) + climbing_stairs(n-2)



def cli(n):
    memo = {}

    def dp(n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n not in memo:
            memo[n] = dp(n-1) + dp(n-2)

        return memo[n]

    return dp(n)
# dp = > top down => 재귀
print(cli(10))