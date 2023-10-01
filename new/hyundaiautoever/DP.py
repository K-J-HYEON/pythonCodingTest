n = int(input())
profit_work = list(map(int, input().split()))
profit_rest = list(map(int, input().split()))

# 현재 날짜까지의 최적 이익을 저장하는 리스트
max_profit = [0] * n
max_profit[0] = profit_work[0]

# 첫 날짜부터 시작해서 마지막 날짜까지 모든 경우의 최적 이익 계산
for i in range(1, n):
    max_profit[i] = max(max_profit[i-1] + profit_rest[i], max_profit[i-1] + profit_work[i], profit_work[i])

# 가장 큰 이익 반환
print(max_profit[-1])