def solution(n, lost, reverse):
    reverse_n = list(set(reverse) - set(lost))
    lost_n = list(set(lost) - set(reverse_n))

    answer = n - lost(lost_n)

    for i in range(n):
        if i-1 in reverse_n:
            answer += 1
            reverse_n.remove(i-1)

        if i+1 in reverse_n:
            answer += 1
            reverse_n.remove(i+1)

    return answer