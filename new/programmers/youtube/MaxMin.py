# https://www.youtube.com/watch?v=xtg34W_lHug&list=PLjWmbjpSjAMDHAQO44bN1DIXQa50JJYxv&index=14

def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))