# https://leetcode.com/problems/longest-consecutive-sequence/ => 추후에 참고

# https://leetcode.com/problems/two-sum/ 문제풀이
def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = True
    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False


two_sum(nums = [4, 1, 9, 7, 8, 2], target = 14)