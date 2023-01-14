# 문제이해 접근방법 코드설계 코드구현

def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    return ans

dailyTemperatures([73, 74, 75, 71, 69])


# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         stack = []
#         ans = [0 for i in range(len(temperatures))]
#         i = 0
#         while i < len(temperatures):
#             if not stack:
#                 stack.append((temperatures[i], i))
#             else:
#                 while stack and stack[-1][0] < temperatures[i]:
#                     index = stack[-1][1]
#                     ans[index] = i - index
#                     stack.pop()
#                 stack.append((temperatures[i], i))
#             i+=1
#         return ans