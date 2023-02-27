def solution(people, limit):
    answer = 0
    people.sort()

    Lidx, Hidx = 0, len(people)-1
    while Lidx < Hidx:
        if people[Lidx] + people[Hidx] <= limit:
            Lidx += 1
            Hidx -= 1
            
        else:
            Hidx -= 1

        answer += 1

    if Hidx == Lidx:
        answer += 1

    return answer


