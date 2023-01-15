# https://leetcode.com/problems/two-sum/
# 코테 적용 방법 => 배열의 다양한 활용
# 1. 반복문
# 2. Sort & TwoPointer
# # o(nlogn)
# 1 2 5 7

def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target = 14))