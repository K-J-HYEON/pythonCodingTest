# 0~19까지 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1~9까지 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)



# 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)


# 좋은 예시
array = [[0] * m for _ in range(n)]

array = [[0] * m] * n