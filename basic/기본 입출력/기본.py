#공백을 기준으로 구분된데이터 입력 받을 때 사용
# list(map(int, input().split()))

# 공백 기준으로 구분된 데이터의 개수 많지 않으면 다음과 같이 사용
# a, b, c = map(int, input().split())



n = int(input())
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)