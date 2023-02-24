# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}

        # dict 저장 시, 일반적으로 enumerate에서 추출되는 key-value를 반대로 저장
        for index, value in enumerate(nums):
            dict[value] = index

        # 다시 enumerate로 추출할 때는 원래 key-value로 추출되니까, 기존에 저장한 (반대로 저장한) dict을 이용해서 index값을 추출해서 return하는 방법
        for index, value in enumerate(nums):
            if target - value in dict and index != dict[target - value]:
                return [index, dict[target - value]]

