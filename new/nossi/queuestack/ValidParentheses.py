# https://leetcode.com/problems/valid-parentheses/

# 시간 복잡도 10 ** 8 넘지말자
# 1<= x <=10**4
# n ** 2 / nlogn / n / log n으로 풀자
# () {} []

# 문제 이해하기 - 접근 방법 - 코드 설계 - 코드 구현
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack