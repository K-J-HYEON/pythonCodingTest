# https://www.youtube.com/watch?v=etERvmy4i24&list=PLjWmbjpSjAMBGpQZo2JnMUDCJL-Ifdtml&index=4

def solution(s):
    # "{{1, 2, 3}, {2, 1} {1, 2, 4, 3}, {2}}"
    # "1, 2, 3}, {2, 1} {1, 2, 4, 3}, {2"
    # ["1, 2, 3", "2, 1", "1,2,4,3", "2"]
    # ["2", "2,1`", "1,2,3", "1,2,4,3"]

    s = s.split("{}")

    answer = []
    for elms in sorted(s.split("},{"), key = lambda x: len(x)):
        for elm in map(int, elms.split(",")):
            if elm not in answer:
                answer.append(elm)
                break

    return answer


