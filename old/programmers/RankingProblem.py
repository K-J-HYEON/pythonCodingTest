# 랭킹 문제 sort를 이용하면 간단하다.
# 처음에 입력되는 점수를 높은 점수와 비교해서 추가할 필요 x
# 매일 입력되는 점수를 rank 리스트 맨 뒤에 추가
# 내림차순으로 정렬하고 정렬된 rank의 길이가 k보다 크면 del 키워드를 이용하여 마지막 랭킹 제거
# answer에 rank[-1]을 추가한다 => 내림차순 정렬했으므로 마지막 값은 최하점

def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        if len(rank) > k:
            del rank[-1]
        answer.append(rank[-1])
    return answer


def solution(k, score):
    q = []
    answer = []
    for s in score:
        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))
    return answer