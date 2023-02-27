# https://www.youtube.com/watch?v=RvPwDIVAhFI&list=PLjWmbjpSjAMDHAQO44bN1DIXQa50JJYxv&index=17

def solution(x):
    answer = [0, 0]

    while not x == "1":
        answer[1] += x.count("0")
        only1s = "1" * x.count("1")

        c = len(only1s)
        x = bin(c)[2:]
        answer[0] += 1

    return answer


def solution(x):
    answer = [0, 0]

    while not x == "1":
        answer[1] += x.count("0")
        x = bin(x.count("1"))[2:]
        answer[0] += 1

    return answer