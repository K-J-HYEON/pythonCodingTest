# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# def solution(clothes):
#     hash_map = {}
#
#     for clothe, type in clothes:
#         hash_map[type] = hash_map.get(type, 0) + 1
#
#
#     answer = 1
#     for type in hash_map:
#         answer *= (hash_map[type] + 1)
#
#     return answer - 1

def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2

        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1