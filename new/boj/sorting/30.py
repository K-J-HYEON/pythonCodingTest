# 1. 양수 N을 구성하는 숫자들 섞어서 30의 배수 되는 최댓값 구함
# 2. N에서 0 없다 => 30 배수 아니고 -1 출력
# 0이 있다 그러면 오른쪽으로 우선 빼고 나머지 수들의 합 3의 배수인지 확인
# 3의 배수 아니면 -1 출력 3의 배수면 나머지 수들 내림차순 정렬

N = int(input())
li = []

for i in N:
    li.append(i)

cnt_zero = li.count('0')

N_sum = 0

for j in N:
    N_sum += int(j)

if cnt_zero == 0:
    print(-1)
elif N_sum % 3 != 0:
    print(-1)
else:
    li.sort(reverse=True)
    print(''.join(li))