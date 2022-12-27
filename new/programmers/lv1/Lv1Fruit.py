## 프로그래머스 과일장수
# 구현 문제
# 사과들 점수 내림차순으로 정렬 => m개씩 잘라가면서 m개 잘린 사과들중에서 가장 작은 값 * m으로 도출
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse= True)

    for i in range(0, len(score), m):
        tmp = score[i:i+m]

        if len(tmp) == m:
            answer += min(tmp) * m

    return answer