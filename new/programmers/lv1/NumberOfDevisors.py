def solution(left, right):
    # 답을 초기화 하고
    answer = 0
    # left에서 right까지 범위를 정호가
    for i in range(left, right + 1):
        # 약수 갯수 담을 칸 초기화 해주고
        now_count = 0;
        # i의 모든 범위를 돌면서
        for j in range(1, i + 1):
            # 약수가 있으면
            if i % j == 0:
                # 약수 갯수 담을 공간에 + 1씩 더해준다.
                now_count += 1;
                print(now_count)

        # 약수의 개수가 짝수이면 answer 에 더해주고
        if now_count % 2 == 0:
            answer += i
        # 약수의 개수가 짝수가 아니면 빼준다.
        else:
            answer -= i

    return answer
