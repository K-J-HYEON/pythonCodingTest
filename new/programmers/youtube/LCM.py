# https://www.youtube.com/watch?v=pVmy04V5KLA&list=PLjWmbjpSjAMDHAQO44bN1DIXQa50JJYxv&index=24

def divs(num):
    DIVS = dict()
    div = 2

    while 1 < num:
        if num % div == 0:
            if div in DIVS:
                DIVS[div] += 1
            else:
                DIVS[divs] = 1

            num = num // div
            div = 2

        else:
            div += 2

def solution(arr):
    LCM = dict()
    for num in arr:
        NUM_DIVS = divs(num)
        for div, count in NUM_DIVS.items():
            if div in LCM:
                LCM[div] = max(LCM[div], count)

            else:
                LCM[div] = count

    answer = 1
    for div, count in LCM.items():
        answer *= div ** count
    return answer