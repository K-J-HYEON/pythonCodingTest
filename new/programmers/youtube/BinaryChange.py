# https://www.youtube.com/watch?v=RvPwDIVAhFI&list=PLjWmbjpSjAMDHAQO44bN1DIXQa50JJYxv&index=17

def solution(x):
    answer = [0, 0]
    while not x == "1":
        answer[1] += x.count("0")
        x = bin(x.count("1"))[2:]
        answer[0] += 1

    return answer

    # count, zero_count = 0, 0
    # while s != '1':
    #     count += 1
    #     zero_count += s.count('0')
    #     s = bin(len(s.replace('0','')))[2:]
    #     print(s)
    # return [count, zero_count]