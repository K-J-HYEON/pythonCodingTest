# https://leetcode.com/problems/two-sum/

# 문제 이해하기 - 접근 방법 - 코드 설계 - 코드 구현

# 문제 이해하기
# int -> 4 바이트 -> 32 = > 2 ** 31
# - 2 ** 31 ~ 2 ** 31 + 1 =>

# 접근 방법

# 코드 설계 => o(n) * o(n) => o(n**2)
# for i in range():
#     for j in range():
# nums[i] + nums[j] == 14 ?
# return T
# 시간 초과 되면 과감하게 포기 / 자료구조 알고리즘 써볼까? 메모리를 사용해서 시간복잡도를 써볼까?
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False


print(twoSum(nums=[4,1,9,7,5,3,16], target=14))