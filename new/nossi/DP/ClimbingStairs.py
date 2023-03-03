# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        def climbStairs(n):
            if n <= 3:
                result = n

            elif n > 3:
                result = climbStairs(n-1) + climbStairs(n-2)
            return result

        return climbStairs(n)