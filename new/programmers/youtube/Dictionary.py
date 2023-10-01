# https://www.youtube.com/watch?v=TnjHHyfCux0&list=PLjWmbjpSjAMDHAQO44bN1DIXQa50JJYxv&index=10

def solution(weights):
    w_dict = dict()
    for w in weights:
        if w in w_dict:
            w_dict[w] += 1

        else:
            w_dict[w] = 1

    print(w_dict)

    answer = 0
    ws = list(w_dict.keys())
    for idx1 in range(len(ws)):
        for idx2 in range(idx1, len(ws)):
            w1, w2 = ws[idx1], ws[idx2]
            if idx1 == idx2 and 1 < w_dict[w1]:
                answer += w_dict[w1] * (w_dict[w1] - 1) // 2
                continue

            if w1 * 2 == w2 * 3:
                answer += w_dict[w1] * w_dict[w2]

            if w1 * 2 == w2 * 4:
                answer += w_dict[w1] * w_dict[w2]

            if w1 * 3 == w2 * 2:
                answer += w_dict[w1] * w_dict[w2]

            if w1 * 3 == w2 * 4:
                answer += w_dict[w1] * w_dict[w2]

            if w1 * 4 == w2 * 2:
                answer += w_dict[w1] * w_dict[w2]

            if w1 * 4 == w2 * 3:
                answer += w_dict[w1] * w_dict[w2]

    return answer

#     count = 0
#     positions = [(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]

#     # 초기화
#     weight_map = {}
#     for weight in weights:
#         weight_map.setdefault(weight, 0)
#         weight_map[weight] += 1

#     for my_weight in weight_map:
#         # 본인이랑 같은 무게의 친구가 있을 경우
#         if weight_map[my_weight] > 1:
#             count += weight_map[my_weight] * (weight_map[my_weight] - 1) // 2
#         # 본인의 몸무게로 평형을 맞출 수 있는 경우
#         for (my_position, friend_position) in positions:
#             expected_friend_weight = my_weight * my_position / friend_position
#             if (expected_friend_weight in weight_map):
#                 count += weight_map[my_weight] * weight_map[expected_friend_weight]
#         # 이미 계산을 끝낸 몸무게는 중복 계산이 되지 않도록 제거해준다
#         weight_map[my_weight] = 0

#     return count
