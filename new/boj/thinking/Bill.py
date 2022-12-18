# 총 가격
total = int(input())
# 총 물건 수
n = int(input())

# 각 물건의 가격과 갯수를 곱한것이 sum
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += a*b


if total == sum:
    print("Yes")
else:
    print("No")