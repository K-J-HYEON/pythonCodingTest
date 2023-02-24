def solution(t, p):
    answer = 0
    n = len(p)
    li = []

    for i in range(0, len(t)-n+1):
        # 0 1 2 3 4
        li.append(t[i:i+n])

    for s in li:
        if int(s) <= int(p):
            answer += 1

    return answer

