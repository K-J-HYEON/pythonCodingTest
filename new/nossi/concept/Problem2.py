# () [] {}를 포함하고 있는 문자열 s가 주어졌울 때, 괄호가 유효한지 아닌지 판별

## 제약조건
# 1 <= s.length <= 10**4
# () = > True
# ))( => False
## 소 중 대 괄호가 있는 상황
# () {} []
# (] +1, -1 => 0 => x 종류에 따라서 달라져야함
# ([]}= > False, {() []} => True => LIFO로 해결하자

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
