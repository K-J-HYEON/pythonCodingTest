# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    answer = 0
    TP = Counter(topping)
    check = set()
    for i in topping:
        TP[i] -= 1
        print(TP)
        if TP[i] == 0: # 토핑 갯수 0이면 삭제
            TP.pop(i)
        if len(TP) == len(check):
            answer += 1

    return answer