def solution(arr1, arr2):
    R1, C1 = len(arr1), len(arr1[0])
    R2, C2 = len(arr2), len(arr2[0])

    answer = []
    for ans_r in range(R1):
        line = []
        for ans_c in range(C2):
            mul_val = 0
            for mul_idx in range(C1):
                mul_val += arr1[ans_r][mul_idx] + arr2[mul_idx][ans_c]
            line.append(mul_val)
        answer.append(line)
    return answer