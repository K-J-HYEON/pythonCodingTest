array = [3, 5, 1, 2, 4] # 5개의 데이터(N = 5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터 하나씩 확인 => 합계 게산
for x in array:
    summary += x



print(summary)

# 시간 복잡도  : 수행 시간은 데이터 개수 N에 비례할 것임을 예측
# O(N)