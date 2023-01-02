# https://velog.io/@kimdukbae/BOJ-11659-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-4-Python
# https://jeongchul.tistory.com/664
# https://www.pymoon.com/entry/%EC%88%98%EC%97%B4%EC%97%90%EC%84%9C-%EC%97%B0%EC%86%8D%EB%90%9C-%EA%B5%AC%EA%B0%84%EC%9D%98-%EC%B5%9C%EB%8C%80-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0


# # 일반 연속 구간 부분수열 최대합
# def partial_sum(arr, a, b):
#     arr = [0] + arr
#     partial_sum = [0] * len(arr)
#
#     for i in range(1, len(arr)):
#         partial_sum[i] = partial_sum[i-1] + arr[i]
#
#     partial_sum = partial_sum[1:]
#     print("partial_sum", partial_sum)
#
#     max_partial_sum = partial_sum[0]
#
#     for b in range(0, len(arr)-1):
#         for a in range(0, b):
#             print(a, b, partial_sum[b] - partial_sum[a-1])
#             max_partial_sum = max(max_partial_sum, partial_sum[b] - partial_sum[a-1])
#
#     print("max partial sum", max_partial_sum)
#
# scores = [-14, 7, 2, 10, -4, 9, -10]
# print("list", scores)
# partial_sum(scores)

# # dp
# def dynamic_partial_sum(arr):
#     cache = [0] * len(arr)
#     cache[0] = arr[0]
#     for i in range(0, len(arr)):
#         cache[i] = max(0, cache[i-1]) + arr[i]
#         print(i, arr[i], cache)
#     print(cache)
#     return max(cache)
#
#
# scores = [-14, 7, 2, 10, -4, 9, -10]
# print("list", scores)
# dynamic_partial_sum(scores)

class Solution:
    def maxSubArray(self, nums):
        """
        """
        temp_sum = nums[0]
        result = nums[0]

        for idx in range(1, len(nums)):
            temp_sum = max(temp_sum + nums[idx], nums[idx])
            result = max(temp_sum, result)
        return result