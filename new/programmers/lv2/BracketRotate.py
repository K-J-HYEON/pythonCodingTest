# https://www.youtube.com/watch?v=3If7lDdQSXI&list=PLjWmbjpSjAMBGpQZo2JnMUDCJL-Ifdtml&index=1

def is_valid(s):
    stack = []
    for char in s:
        if stack and stack[-1] == '[' and char == ']':
            del stack[-1]

        elif stack and stack[-1] == "{" and char == "}":
            del stack[-1]

        elif stack and stack[-1] == "(" and char == ")":
            del stack[-1]

        else:
            stack.append(char)

    return stack == []


def solution(s):
    answer = 0

    for x in range(len(s)):
        # left s[:x]
        # right s[x:]

        if is_valid(s[x:] + s[:x]):
            answer += 1

    return answer